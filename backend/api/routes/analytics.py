from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from api.database import get_db

from api.schemas.analytics import (
    DriverComparisonResponse,
    FastestLapResponse,
    PerformanceScoreResponse,
    RaceSummaryResponse,
    TopSpeedResponse,
)

from api.services.analytics_service import (
    compare_drivers,
    get_driver_performance_scores,
    get_fastest_laps,
    get_race_summary,
    get_top_speeds,
)

router = APIRouter(
    prefix="/analytics",
    tags=["Analytics"],
)


# --------------------------------------------------
# Fastest Laps
# --------------------------------------------------

@router.get(
    "/fastest-laps/{session_key}",
    response_model=list[FastestLapResponse],
)
def fastest_laps(
    session_key: int,
    db: Session = Depends(get_db),
):
    return get_fastest_laps(
        db,
        session_key,
    )


# --------------------------------------------------
# Top Speeds
# --------------------------------------------------

@router.get(
    "/top-speeds/{session_key}",
    response_model=list[TopSpeedResponse],
)
def top_speeds(
    session_key: int,
    db: Session = Depends(get_db),
):
    return get_top_speeds(
        db,
        session_key,
    )


# --------------------------------------------------
# Driver Comparison
# --------------------------------------------------

@router.get(
    "/compare",
    response_model=DriverComparisonResponse,
)
def compare(
    session_key: int,
    driver1: int,
    driver2: int,
    db: Session = Depends(get_db),
):
    return compare_drivers(
        db,
        session_key,
        driver1,
        driver2,
    )


# --------------------------------------------------
# Race Summary
# --------------------------------------------------

@router.get(
    "/race-summary/{session_key}",
    response_model=RaceSummaryResponse,
)
def race_summary(
    session_key: int,
    db: Session = Depends(get_db),
):
    return get_race_summary(
        db,
        session_key,
    )


# --------------------------------------------------
# Driver Performance Score
# --------------------------------------------------

@router.get(
    "/performance-score/{session_key}",
    response_model=list[PerformanceScoreResponse],
)
def performance_score(
    session_key: int,
    db: Session = Depends(get_db),
):
    return get_driver_performance_scores(
        db,
        session_key,
    )