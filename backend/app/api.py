from fastapi import APIRouter, Query
from app.services.session_service import (
    get_seasons,
    get_events,
    get_sessions,
    get_drivers,
)

from app.services.telemetry_service import get_driver_telemetry


router = APIRouter(
    prefix="/api",
    tags=["Telemetry"],
)


@router.get("/telemetry")
def get_telemetry(
    year: int = Query(2024),
    grand_prix: str = Query("Monaco"),
    session_type: str = Query("Q"),
    driver: str = Query("VER"),
):
    """
    Returns telemetry for the selected driver.

    Currently uses offline JSON.
    Later this service can load data from
    FastF1/OpenF1 without changing this API.
    """

    return get_driver_telemetry(
        year=year,
        grand_prix=grand_prix,
        session_type=session_type,
        driver=driver,
    )
@router.get("/seasons")
def seasons():
    return get_seasons()
@router.get("/events")
def events(season: str):
    return get_events(season)

@router.get("/sessions")
def sessions(
    season: str,
    event: str,
):
    return get_sessions(season, event)

@router.get("/drivers")
def drivers(
    season: str,
    event: str,
    session: str,
):
    return get_drivers(
        season,
        event,
        session,
    )