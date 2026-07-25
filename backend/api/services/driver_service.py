from sqlalchemy.orm import Session

from database.models.driver import Driver


def get_all_drivers(db: Session):
    return db.query(Driver).all()


def get_driver(
    db: Session,
    session_key: int,
    driver_number: int,
):
    return (
        db.query(Driver)
        .filter(
            Driver.session_key == session_key,
            Driver.driver_number == driver_number,
        )
        .first()
    )


def get_drivers_by_session(
    db: Session,
    session_key: int,
):
    return (
        db.query(Driver)
        .filter(Driver.session_key == session_key)
        .all()
    )


def get_drivers_by_team(
    db: Session,
    team_name: str,
):
    return (
        db.query(Driver)
        .filter(Driver.team_name == team_name)
        .all()
    )