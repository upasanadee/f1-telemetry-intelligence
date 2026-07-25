from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from api.database import get_db
from api.schemas.lap import LapResponse
from api.services.lap_service import (
    get_all_laps,
    get_driver_laps,
    get_fastest_lap,
    get_laps_by_session,
    get_single_lap,
)

router = APIRouter(
    prefix="/laps",
    tags=["Laps"],
)


@router.get("", response_model=list[LapResponse])
def laps(
    db: Session = Depends(get_db),
):
    return get_all_laps(db)


@router.get("/session/{session_key}", response_model=list[LapResponse])
def laps_by_session(
    session_key: int,
    db: Session = Depends(get_db),
):
    return get_laps_by_session(db, session_key)


@router.get(
    "/{session_key}/{driver_number}",
    response_model=list[LapResponse],
)
def driver_laps(
    session_key: int,
    driver_number: int,
    db: Session = Depends(get_db),
):
    return get_driver_laps(
        db,
        session_key,
        driver_number,
    )


@router.get(
    "/{session_key}/{driver_number}/fastest",
    response_model=LapResponse,
)
def fastest_lap(
    session_key: int,
    driver_number: int,
    db: Session = Depends(get_db),
):
    lap = get_fastest_lap(
        db,
        session_key,
        driver_number,
    )

    if lap is None:
        raise HTTPException(
            status_code=404,
            detail="No laps found",
        )

    return lap


@router.get(
    "/{session_key}/{driver_number}/{lap_number}",
    response_model=LapResponse,
)
def single_lap(
    session_key: int,
    driver_number: int,
    lap_number: int,
    db: Session = Depends(get_db),
):
    lap = get_single_lap(
        db,
        session_key,
        driver_number,
        lap_number,
    )

    if lap is None:
        raise HTTPException(
            status_code=404,
            detail="Lap not found",
        )

    return lap