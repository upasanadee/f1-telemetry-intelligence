from fastapi import APIRouter, Query
import json
from pathlib import Path

router = APIRouter(prefix="/api", tags=["Telemetry"])


@router.get("/telemetry")
def get_telemetry(
    gp: str = Query("Monaco"),
    session: str = Query("Q"),
    driver1: str = Query("VER"),
    driver2: str = Query("HAM"),
):
    """
    Temporary endpoint.

    Later:
    - Load FastF1 session
    - Process telemetry
    - Run AI models
    """

    json_path = (
        Path(__file__).parent.parent
        / "data"
        / "f1_dashboard_data.json"
    )

    with open(json_path) as f:
        data = json.load(f)

    return data