from datetime import timedelta
import os

import numpy as np
import pandas as pd

from database.connection import SessionLocal
from database.models.lap import Lap
from database.models.car_data import CarData

db = SessionLocal()

# =====================================================
# Output folders
# =====================================================

OUTPUT_DIR = "ml/dl/sequences"

os.makedirs(
    OUTPUT_DIR,
    exist_ok=True,
)

labels = []

# =====================================================
# Get valid laps
# =====================================================

laps = (
    db.query(Lap)
    .filter(
        Lap.date_start.isnot(None),
        Lap.lap_duration.isnot(None),
    )
    .all()
)

print(f"Found {len(laps)} laps")

saved = 0

# =====================================================
# Process each lap
# =====================================================

for lap in laps:

    lap_end = (
        lap.date_start
        + timedelta(
            seconds=float(lap.lap_duration)
        )
    )

    telemetry = (
        db.query(CarData)
        .filter(
            CarData.session_key == lap.session_key,
            CarData.driver_number == lap.driver_number,
            CarData.date >= lap.date_start,
            CarData.date <= lap_end,
        )
        .order_by(CarData.date)
        .all()
    )

    # Skip empty laps
    if len(telemetry) < 50:
        continue

    sequence = []

    start_time = telemetry[0].date

    for sample in telemetry:

        elapsed = (
            sample.date - start_time
        ).total_seconds()

        sequence.append(
            [
                elapsed,
                sample.speed if sample.speed is not None else 0,
                sample.rpm if sample.rpm is not None else 0,
                sample.n_gear if sample.n_gear is not None else 0,
                sample.throttle if sample.throttle is not None else 0,
                sample.brake if sample.brake is not None else 0,
                sample.drs if sample.drs is not None else 0,
            ]
        )

    sequence = np.array(
        sequence,
        dtype=np.float32,
    )

    filename = (
        f"{lap.session_key}_"
        f"{lap.driver_number}_"
        f"{lap.lap_number}.npy"
    )

    np.save(
        os.path.join(
            OUTPUT_DIR,
            filename,
        ),
        sequence,
    )

    labels.append(
        {
            "file": filename,
            "session_key": lap.session_key,
            "driver_number": lap.driver_number,
            "lap_number": lap.lap_number,
            "lap_duration": lap.lap_duration,
            "num_samples": len(sequence),
        }
    )

    saved += 1

# =====================================================
# Save labels
# =====================================================

labels_df = pd.DataFrame(labels)

labels_df.to_csv(
    "ml/dl/labels.csv",
    index=False,
)

print()

print(f"Saved {saved} lap sequences.")

print(f"Labels: {len(labels_df)}")

print()

print(labels_df.head())