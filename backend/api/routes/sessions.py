from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from api.database import get_db
from api.schemas.session import SessionResponse
from api.services.session_service import (
    get_all_sessions,
    get_session_by_id,
    get_sessions_by_meeting,
)

router = APIRouter(
    prefix="/sessions",
    tags=["Sessions"],
)


@router.get("", response_model=list[SessionResponse])
def get_sessions(
    db: Session = Depends(get_db),
):
    return get_all_sessions(db)


@router.get("/meeting/{meeting_key}", response_model=list[SessionResponse])
def get_sessions_for_meeting(
    meeting_key: int,
    db: Session = Depends(get_db),
):
    return get_sessions_by_meeting(db, meeting_key)


@router.get("/{session_key}", response_model=SessionResponse)
def get_session(
    session_key: int,
    db: Session = Depends(get_db),
):
    session = get_session_by_id(db, session_key)

    if session is None:
        raise HTTPException(
            status_code=404,
            detail="Session not found",
        )

    return session