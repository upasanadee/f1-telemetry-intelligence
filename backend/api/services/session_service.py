from sqlalchemy.orm import Session
from database.models.session import Session as SessionModel


def get_all_sessions(db: Session):
    return db.query(SessionModel).all()


def get_session_by_id(db: Session, session_key: int):
    return (
        db.query(SessionModel)
        .filter(SessionModel.session_key == session_key)
        .first()
    )


def get_sessions_by_meeting(db: Session, meeting_key: int):
    return (
        db.query(SessionModel)
        .filter(SessionModel.meeting_key == meeting_key)
        .all()
    )