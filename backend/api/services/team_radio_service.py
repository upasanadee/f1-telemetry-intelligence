from sqlalchemy.orm import Session

from database.models.team_radio import TeamRadio


def get_team_radio_by_session(
    db: Session,
    session_key: int,
):
    return (
        db.query(TeamRadio)
        .filter(TeamRadio.session_key == session_key)
        .order_by(TeamRadio.driver_number, TeamRadio.date)
        .all()
    )


def get_driver_team_radio(
    db: Session,
    session_key: int,
    driver_number: int,
):
    return (
        db.query(TeamRadio)
        .filter(
            TeamRadio.session_key == session_key,
            TeamRadio.driver_number == driver_number,
        )
        .order_by(TeamRadio.date)
        .all()
    )


def get_latest_team_radio(
    db: Session,
    session_key: int,
    driver_number: int,
):
    return (
        db.query(TeamRadio)
        .filter(
            TeamRadio.session_key == session_key,
            TeamRadio.driver_number == driver_number,
        )
        .order_by(TeamRadio.date.desc())
        .first()
    )