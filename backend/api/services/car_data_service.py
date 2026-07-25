from sqlalchemy.orm import Session

from database.models.car_data import CarData


def get_car_data_by_session(
    db: Session,
    session_key: int,
    limit: int = 1000,
    offset: int = 0,
):
    return (
        db.query(CarData)
        .filter(CarData.session_key == session_key)
        .order_by(CarData.driver_number, CarData.date)
        .offset(offset)
        .limit(limit)
        .all()
    )


def get_driver_car_data(
    db: Session,
    session_key: int,
    driver_number: int,
    limit: int = 1000,
    offset: int = 0,
):
    return (
        db.query(CarData)
        .filter(
            CarData.session_key == session_key,
            CarData.driver_number == driver_number,
        )
        .order_by(CarData.date)
        .offset(offset)
        .limit(limit)
        .all()
    )


def get_latest_car_data(
    db: Session,
    session_key: int,
    driver_number: int,
):
    return (
        db.query(CarData)
        .filter(
            CarData.session_key == session_key,
            CarData.driver_number == driver_number,
        )
        .order_by(CarData.date.desc())
        .first()
    )