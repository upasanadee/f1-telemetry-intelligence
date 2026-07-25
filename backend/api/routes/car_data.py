from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from api.database import get_db
from api.schemas.car_data import CarDataResponse
from api.services.car_data_service import (
    get_car_data_by_session,
    get_driver_car_data,
    get_latest_car_data,
)

router = APIRouter(
    prefix="/car-data",
    tags=["Car Data"],
)


# GET /car-data/session/{session_key}
@router.get(
    "/session/{session_key}",
    response_model=list[CarDataResponse],
)
def session_car_data(
    session_key: int,
    limit: int = 1000,
    offset: int = 0,
    db: Session = Depends(get_db),
):
    return get_car_data_by_session(
        db,
        session_key,
        limit,
        offset,
    )


# GET /car-data/{session_key}/{driver_number}
@router.get(
    "/{session_key}/{driver_number}",
    response_model=list[CarDataResponse],
)
def driver_car_data(
    session_key: int,
    driver_number: int,
    limit: int = 1000,
    offset: int = 0,
    db: Session = Depends(get_db),
):
    return get_driver_car_data(
        db,
        session_key,
        driver_number,
        limit,
        offset,
    )


# GET /car-data/{session_key}/{driver_number}/latest
@router.get(
    "/{session_key}/{driver_number}/latest",
    response_model=CarDataResponse,
)
def latest_car_data(
    session_key: int,
    driver_number: int,
    db: Session = Depends(get_db),
):
    data = get_latest_car_data(
        db,
        session_key,
        driver_number,
    )

    if data is None:
        raise HTTPException(
            status_code=404,
            detail="Car data not found",
        )

    return data