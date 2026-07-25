from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from api.database import get_db
from api.schemas.analytics import FastestLapResponse
from api.services.analytics_service import get_fastest_laps

router = APIRouter(
    prefix="/analytics",
    tags=["Analytics"],
)


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