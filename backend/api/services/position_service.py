from sqlalchemy.orm import Session

from database.models.position import Position


def get_positions_by_session(
    db: Session,
    session_key: int,
    limit: int = 1000,
    offset: int = 0,
):
    return (
        db.query(Position)
        .filter(Position.session_key == session_key)
        .order_by(Position.driver_number, Position.date)
        .offset(offset)
        .limit(limit)
        .all()
    )


def get_driver_positions(
    db: Session,
    session_key: int,
    driver_number: int,
    limit: int = 1000,
    offset: int = 0,
):
    return (
        db.query(Position)
        .filter(
            Position.session_key == session_key,
            Position.driver_number == driver_number,
        )
        .order_by(Position.date)
        .offset(offset)
        .limit(limit)
        .all()
    )


def get_latest_position(
    db: Session,
    session_key: int,
    driver_number: int,
):
    return (
        db.query(Position)
        .filter(
            Position.session_key == session_key,
            Position.driver_number == driver_number,
        )
        .order_by(Position.date.desc())
        .first()
    )