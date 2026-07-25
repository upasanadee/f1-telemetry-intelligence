from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from api.database import get_db
from api.schemas.team_radio import TeamRadioResponse
from api.services.team_radio_service import (
    get_driver_team_radio,
    get_latest_team_radio,
    get_team_radio_by_session,
)

router = APIRouter(
    prefix="/team-radio",
    tags=["Team Radio"],
)


@router.get(
    "/session/{session_key}",
    response_model=list[TeamRadioResponse],
)
def session_team_radio(
    session_key: int,
    db: Session = Depends(get_db),
):
    return get_team_radio_by_session(
        db,
        session_key,
    )


@router.get(
    "/{session_key}/{driver_number}",
    response_model=list[TeamRadioResponse],
)
def driver_team_radio(
    session_key: int,
    driver_number: int,
    db: Session = Depends(get_db),
):
    return get_driver_team_radio(
        db,
        session_key,
        driver_number,
    )


@router.get(
    "/{session_key}/{driver_number}/latest",
    response_model=TeamRadioResponse,
)
def latest_team_radio(
    session_key: int,
    driver_number: int,
    db: Session = Depends(get_db),
):
    radio = get_latest_team_radio(
        db,
        session_key,
        driver_number,
    )

    if radio is None:
        raise HTTPException(
            status_code=404,
            detail="Team radio not found",
        )

    return radio