from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from api.database import get_db
from api.schemas.position import PositionResponse
from api.services.position_service import (
    get_driver_positions,
    get_latest_position,
    get_positions_by_session,
)

router = APIRouter(
    prefix="/positions",
    tags=["Positions"],
)


@router.get(
    "/session/{session_key}",
    response_model=list[PositionResponse],
)
def session_positions(
    session_key: int,
    limit: int = 1000,
    offset: int = 0,
    db: Session = Depends(get_db),
):
    return get_positions_by_session(
        db,
        session_key,
        limit,
        offset,
    )


@router.get(
    "/{session_key}/{driver_number}",
    response_model=list[PositionResponse],
)
def driver_positions(
    session_key: int,
    driver_number: int,
    limit: int = 1000,
    offset: int = 0,
    db: Session = Depends(get_db),
):
    return get_driver_positions(
        db,
        session_key,
        driver_number,
        limit,
        offset,
    )


@router.get(
    "/{session_key}/{driver_number}/latest",
    response_model=PositionResponse,
)
def latest_position(
    session_key: int,
    driver_number: int,
    db: Session = Depends(get_db),
):
    position = get_latest_position(
        db,
        session_key,
        driver_number,
    )

    if position is None:
        raise HTTPException(
            status_code=404,
            detail="Position not found",
        )

    return position