from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from api.database import get_db
from api.schemas.meeting import MeetingResponse
from api.services.meeting_service import (
    get_all_meetings,
    get_meeting_by_id,
    get_meetings_by_year,
)

router = APIRouter(prefix="/meetings", tags=["Meetings"])


@router.get("", response_model=list[MeetingResponse])
def get_meetings(
    year: int | None = None,
    db: Session = Depends(get_db),
):
    if year:
        return get_meetings_by_year(db, year)

    return get_all_meetings(db)


@router.get("/{meeting_key}", response_model=MeetingResponse)
def get_meeting(
    meeting_key: int,
    db: Session = Depends(get_db),
):
    meeting = get_meeting_by_id(db, meeting_key)

    if meeting is None:
        raise HTTPException(
            status_code=404,
            detail="Meeting not found",
        )

    return meeting