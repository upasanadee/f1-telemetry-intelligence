from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from api.database import get_db
from api.schemas.weather import WeatherResponse
from api.services.weather_service import (
    get_latest_weather,
    get_weather_by_session,
)

router = APIRouter(
    prefix="/weather",
    tags=["Weather"],
)


@router.get(
    "/session/{session_key}",
    response_model=list[WeatherResponse],
)
def session_weather(
    session_key: int,
    db: Session = Depends(get_db),
):
    return get_weather_by_session(
        db,
        session_key,
    )


@router.get(
    "/latest/{session_key}",
    response_model=WeatherResponse,
)
def latest_weather(
    session_key: int,
    db: Session = Depends(get_db),
):
    weather = get_latest_weather(
        db,
        session_key,
    )

    if weather is None:
        raise HTTPException(
            status_code=404,
            detail="Weather data not found",
        )

    return weather