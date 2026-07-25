from sqlalchemy.orm import Session

from database.models.meeting import Meeting


def get_all_meetings(db: Session):
    return db.query(Meeting).all()


def get_meeting_by_id(db: Session, meeting_key: int):
    return (
        db.query(Meeting)
        .filter(Meeting.meeting_key == meeting_key)
        .first()
    )


def get_meetings_by_year(db: Session, year: int):
    return (
        db.query(Meeting)
        .filter(Meeting.year == year)
        .all()
    )