import json
from pathlib import Path

DATA_FILE = (
    Path(__file__).resolve().parent.parent.parent
    / "data"
    / "f1_dashboard_data.json"
)


def get_driver_telemetry(
    year: int = None,
    grand_prix: str = None,
    session_type: str = None,
    driver: str = None,
):
    """
    Returns telemetry from the offline JSON dataset.
    """

    with open(DATA_FILE, "r") as f:
        data = json.load(f)

    return {
        "distance": data["distance"],
        "speed": data["speed_trace"],
        "throttle": data["throttle_trace"],
        "brake": data["brake_trace"],
        "tire": data["tire_trace"],
        "engine": data["engine_trace"],
        "driver1": data["driver1"],
        "driver2": data["driver2"],
        "avg_speed": data["avg_speed"],
        "top_speed": data["top_speed"],
        "insights": data["insights"],
        "prediction": data["prediction"],
    }