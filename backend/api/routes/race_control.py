from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from api.database import get_db
from api.schemas.race_control import RaceControlResponse
from api.services.race_control_service import (
    get_latest_race_control,
    get_race_control_by_category,
    get_race_control_by_flag,
    get_race_control_by_session,
)

router = APIRouter(
    prefix="/race-control",
    tags=["Race Control"],
)


@router.get(
    "/session/{session_key}",
    response_model=list[RaceControlResponse],
)
def session_race_control(
    session_key: int,
    db: Session = Depends(get_db),
):
    return get_race_control_by_session(
        db,
        session_key,
    )


@router.get(
    "/category/{category}",
    response_model=list[RaceControlResponse],
)
def category_race_control(
    category: str,
    db: Session = Depends(get_db),
):
    return get_race_control_by_category(
        db,
        category,
    )


@router.get(
    "/flag/{flag}",
    response_model=list[RaceControlResponse],
)
def flag_race_control(
    flag: str,
    db: Session = Depends(get_db),
):
    return get_race_control_by_flag(
        db,
        flag,
    )


@router.get(
    "/latest/{session_key}",
    response_model=RaceControlResponse,
)
def latest_race_control(
    session_key: int,
    db: Session = Depends(get_db),
):
    event = get_latest_race_control(
        db,
        session_key,
    )

    if event is None:
        raise HTTPException(
            status_code=404,
            detail="Race control event not found",
        )

    return event