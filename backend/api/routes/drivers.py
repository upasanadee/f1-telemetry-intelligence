from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from api.database import get_db
from api.schemas.driver import DriverResponse
from api.services.driver_service import (
    get_all_drivers,
    get_driver,
    get_drivers_by_session,
    get_drivers_by_team,
)

router = APIRouter(
    prefix="/drivers",
    tags=["Drivers"],
)


@router.get("", response_model=list[DriverResponse])
def drivers(
    team: str | None = None,
    db: Session = Depends(get_db),
):
    if team:
        return get_drivers_by_team(db, team)

    return get_all_drivers(db)


@router.get("/session/{session_key}", response_model=list[DriverResponse])
def drivers_for_session(
    session_key: int,
    db: Session = Depends(get_db),
):
    return get_drivers_by_session(db, session_key)


@router.get("/{session_key}/{driver_number}", response_model=DriverResponse)
def driver(
    session_key: int,
    driver_number: int,
    db: Session = Depends(get_db),
):
    result = get_driver(
        db,
        session_key,
        driver_number,
    )

    if result is None:
        raise HTTPException(
            status_code=404,
            detail="Driver not found",
        )

    return result