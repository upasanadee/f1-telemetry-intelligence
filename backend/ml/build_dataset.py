import pandas as pd
import numpy as np

from database.connection import SessionLocal

from database.models.session import Session
from database.models.driver import Driver
from database.models.lap import Lap
from database.models.car_data import CarData
from database.models.weather import Weather


db = SessionLocal()

def compute_lap_features(session_key, driver_number):
    laps = (
        db.query(Lap)
        .filter(
            Lap.session_key == session_key,
            Lap.driver_number == driver_number,
            Lap.lap_duration.isnot(None),
        )
        .all()
    )

    if not laps:
        return {
            "fastest_lap": None,
            "average_lap": None,
            "lap_std": None,
            "total_laps": 0,
        }

    lap_times = np.array(
        [lap.lap_duration for lap in laps],
        dtype=float,
    )

    return {
        "fastest_lap": float(np.min(lap_times)),
        "average_lap": float(np.mean(lap_times)),
        "lap_std": float(np.std(lap_times)),
        "total_laps": len(lap_times),
    }
def compute_car_features(session_key, driver_number):
    telemetry = (
        db.query(CarData)
        .filter(
            CarData.session_key == session_key,
            CarData.driver_number == driver_number,
        )
        .all()
    )

    if not telemetry:
        return {
            "average_speed": None,
            "max_speed": None,
            "average_rpm": None,
            "average_gear": None,
            "average_throttle": None,
            "average_brake": None,
            "drs_usage": None,
        }

    speed = np.array(
        [x.speed for x in telemetry if x.speed is not None],
        dtype=float,
    )

    rpm = np.array(
        [x.rpm for x in telemetry if x.rpm is not None],
        dtype=float,
    )

    gear = np.array(
        [x.n_gear for x in telemetry if x.n_gear is not None],
        dtype=float,
    )

    throttle = np.array(
        [x.throttle for x in telemetry if x.throttle is not None],
        dtype=float,
    )

    brake = np.array(
        [x.brake for x in telemetry if x.brake is not None],
        dtype=float,
    )

    drs = np.array(
        [x.drs for x in telemetry if x.drs is not None],
        dtype=float,
    )

    return {
        "average_speed": float(np.mean(speed)),
        "max_speed": float(np.max(speed)),
        "average_rpm": float(np.mean(rpm)),
        "average_gear": float(np.mean(gear)),
        "average_throttle": float(np.mean(throttle)),
        "average_brake": float(np.mean(brake)),
        "drs_usage": float(np.mean(drs > 0)),
    }
def compute_weather_features(session_key):
    weather = (
        db.query(Weather)
        .filter(
            Weather.session_key == session_key,
        )
        .all()
    )

    if not weather:
        return {
            "track_temp": None,
            "air_temp": None,
            "humidity": None,
            "wind_speed": None,
        }

    return {
        "track_temp": np.mean(
            [w.track_temperature for w in weather if w.track_temperature is not None]
        ),
        "air_temp": np.mean(
            [w.air_temperature for w in weather if w.air_temperature is not None]
        ),
        "humidity": np.mean(
            [w.humidity for w in weather if w.humidity is not None]
        ),
        "wind_speed": np.mean(
            [w.wind_speed for w in weather if w.wind_speed is not None]
        ),
    }
def build_dataset():

    rows = []

    sessions = db.query(Session).all()

    print(f"Found {len(sessions)} sessions")

    for session in sessions:

        print(session.session_key)

        drivers = (
            db.query(Driver)
            .filter(
                Driver.session_key == session.session_key,
            )
            .all()
        )

        weather = compute_weather_features(
            session.session_key
        )

        for driver in drivers:

            lap = compute_lap_features(
                session.session_key,
                driver.driver_number,
            )

            car = compute_car_features(
                session.session_key,
                driver.driver_number,
            )

            rows.append(
                {
                    "session_key": session.session_key,
                    "driver_number": driver.driver_number,
                    "driver_name": driver.full_name,
                    "team_name": driver.team_name,
                    **lap,
                    **car,
                    **weather,
                }
            )

    df = pd.DataFrame(rows)

    df.to_csv(
        "ml/dataset.csv",
        index=False,
    )

    print(df.head())

    print()

    print(df.shape)

    print()

    print("Dataset saved!")

if __name__ == "__main__":
    build_dataset()