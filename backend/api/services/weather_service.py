from sqlalchemy.orm import Session

from database.models.weather import Weather


def get_weather_by_session(
    db: Session,
    session_key: int,
):
    return (
        db.query(Weather)
        .filter(Weather.session_key == session_key)
        .order_by(Weather.date)
        .all()
    )


def get_latest_weather(
    db: Session,
    session_key: int,
):
    return (
        db.query(Weather)
        .filter(Weather.session_key == session_key)
        .order_by(Weather.date.desc())
        .first()
    )