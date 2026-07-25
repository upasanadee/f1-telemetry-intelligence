from sqlalchemy.orm import Session

from database.models.race_control import RaceControl


def get_race_control_by_session(
    db: Session,
    session_key: int,
):
    return (
        db.query(RaceControl)
        .filter(RaceControl.session_key == session_key)
        .order_by(RaceControl.date)
        .all()
    )


def get_latest_race_control(
    db: Session,
    session_key: int,
):
    return (
        db.query(RaceControl)
        .filter(RaceControl.session_key == session_key)
        .order_by(RaceControl.date.desc())
        .first()
    )


def get_race_control_by_category(
    db: Session,
    category: str,
):
    return (
        db.query(RaceControl)
        .filter(RaceControl.category == category)
        .order_by(RaceControl.date.desc())
        .all()
    )


def get_race_control_by_flag(
    db: Session,
    flag: str,
):
    return (
        db.query(RaceControl)
        .filter(RaceControl.flag == flag)
        .order_by(RaceControl.date.desc())
        .all()
    )