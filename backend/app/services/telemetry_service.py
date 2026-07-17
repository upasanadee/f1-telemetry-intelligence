import pandas as pd

from app.services.fastf1_service import load_session


def get_driver_telemetry(
    year: int,
    grand_prix: str,
    session_type: str,
    driver: str,
):
    """
    Returns telemetry for the driver's fastest lap.
    """

    session = load_session(
        year,
        grand_prix,
        session_type,
    )

    laps = session.laps.pick_drivers(driver)

    if laps.empty:
        raise ValueError(f"No laps found for driver '{driver}'")

    fastest = laps.pick_fastest()

    telemetry = (
        fastest
        .get_car_data()
        .add_distance()
    )

    telemetry = telemetry.fillna(0)

    return {
        "distance": telemetry["Distance"].tolist(),
        "speed": telemetry["Speed"].tolist(),
        "rpm": telemetry["RPM"].tolist(),
        "throttle": telemetry["Throttle"].tolist(),
        "brake": telemetry["Brake"].astype(int).tolist(),
        "gear": telemetry["nGear"].tolist(),
    }