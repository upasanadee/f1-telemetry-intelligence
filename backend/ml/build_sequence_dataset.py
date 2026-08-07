import os
import numpy as np

from database.connection import SessionLocal
from database.models.driver import Driver
from database.models.car_data import CarData

db = SessionLocal()

# =====================================================
# Configuration
# =====================================================

OUTPUT_DIR = "ml/sequences"

os.makedirs(OUTPUT_DIR, exist_ok=True)

# =====================================================
# Build Dataset
# =====================================================

drivers = db.query(Driver).all()

print(f"Found {len(drivers)} driver sessions")

saved = 0

for driver in drivers:

    telemetry = (
        db.query(CarData)
        .filter(
            CarData.session_key == driver.session_key,
            CarData.driver_number == driver.driver_number,
        )
        .order_by(CarData.date)
        .all()
    )

    if len(telemetry) < 100:
        continue

    sequence = []

    for sample in telemetry:

        sequence.append([
            sample.speed or 0,
            sample.rpm or 0,
            sample.n_gear or 0,
            sample.throttle or 0,
            sample.brake or 0,
            sample.drs or 0,
        ])

    sequence = np.array(
        sequence,
        dtype=np.float32,
    )

    filename = (
        f"{driver.session_key}_"
        f"{driver.driver_number}.npy"
    )

    np.save(
        os.path.join(
            OUTPUT_DIR,
            filename,
        ),
        sequence,
    )

    saved += 1

print()
print(f"Saved {saved} telemetry sequences.")
print(f"Directory: {OUTPUT_DIR}")