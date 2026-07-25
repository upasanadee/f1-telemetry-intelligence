from sqlalchemy.orm import Session

from database.models.lap import Lap


def get_all_laps(db: Session):
    return db.query(Lap).all()


def get_laps_by_session(
    db: Session,
    session_key: int,
):
    return (
        db.query(Lap)
        .filter(Lap.session_key == session_key)
        .all()
    )


def get_driver_laps(
    db: Session,
    session_key: int,
    driver_number: int,
):
    return (
        db.query(Lap)
        .filter(
            Lap.session_key == session_key,
            Lap.driver_number == driver_number,
        )
        .order_by(Lap.lap_number)
        .all()
    )


def get_single_lap(
    db: Session,
    session_key: int,
    driver_number: int,
    lap_number: int,
):
    return (
        db.query(Lap)
        .filter(
            Lap.session_key == session_key,
            Lap.driver_number == driver_number,
            Lap.lap_number == lap_number,
        )
        .first()
    )


def get_fastest_lap(
    db: Session,
    session_key: int,
    driver_number: int,
):
    return (
        db.query(Lap)
        .filter(
            Lap.session_key == session_key,
            Lap.driver_number == driver_number,
            Lap.lap_duration.isnot(None),
        )
        .order_by(Lap.lap_duration.asc())
        .first()
    )