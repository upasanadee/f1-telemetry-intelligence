from sqlalchemy import func
from sqlalchemy.orm import Session

from database.models.car_data import CarData
from database.models.driver import Driver
from database.models.lap import Lap


def get_fastest_laps(
    db: Session,
    session_key: int,
):
    rows = (
        db.query(Lap, Driver)
        .join(
            Driver,
            (Lap.session_key == Driver.session_key)
            & (Lap.driver_number == Driver.driver_number),
        )
        .filter(
            Lap.session_key == session_key,
            Lap.lap_duration.isnot(None),
        )
        .order_by(
            Lap.driver_number,
            Lap.lap_duration,
        )
        .all()
    )

    fastest = {}

    for lap, driver in rows:
        if lap.driver_number not in fastest:
            fastest[lap.driver_number] = {
                "driver_number": lap.driver_number,
                "driver_name": driver.full_name,
                "team_name": driver.team_name,
                "lap_number": lap.lap_number,
                "lap_duration": lap.lap_duration,
                "duration_sector_1": lap.duration_sector_1,
                "duration_sector_2": lap.duration_sector_2,
                "duration_sector_3": lap.duration_sector_3,
            }

    return list(fastest.values())


def get_top_speeds(
    db: Session,
    session_key: int,
):
    rows = (
        db.query(
            Driver.driver_number,
            Driver.full_name,
            Driver.team_name,
            func.max(CarData.speed).label("top_speed"),
        )
        .join(
            CarData,
            (Driver.session_key == CarData.session_key)
            & (Driver.driver_number == CarData.driver_number),
        )
        .filter(Driver.session_key == session_key)
        .group_by(
            Driver.driver_number,
            Driver.full_name,
            Driver.team_name,
        )
        .order_by(func.max(CarData.speed).desc())
        .all()
    )

    return [
        {
            "driver_number": row.driver_number,
            "driver_name": row.full_name,
            "team_name": row.team_name,
            "top_speed": row.top_speed,
        }
        for row in rows
    ]