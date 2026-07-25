from sqlalchemy import func
from sqlalchemy.orm import Session

from database.models.car_data import CarData
from database.models.driver import Driver
from database.models.lap import Lap
from database.models.weather import Weather
from database.models.race_control import RaceControl


# --------------------------------------------------
# Fastest Laps
# --------------------------------------------------

def get_fastest_laps(
    db: Session,
    session_key: int,
):
    rows = (
        db.query(Lap, Driver)
        .join(
            Driver,
            (Lap.session_key == Driver.session_key)
            & (Lap.driver_number == Driver.driver_number),
        )
        .filter(
            Lap.session_key == session_key,
            Lap.lap_duration.isnot(None),
        )
        .order_by(
            Lap.driver_number,
            Lap.lap_duration,
        )
        .all()
    )

    fastest = {}

    for lap, driver in rows:
        if lap.driver_number not in fastest:
            fastest[lap.driver_number] = {
                "driver_number": lap.driver_number,
                "driver_name": driver.full_name,
                "team_name": driver.team_name,
                "lap_number": lap.lap_number,
                "lap_duration": lap.lap_duration,
                "duration_sector_1": lap.duration_sector_1,
                "duration_sector_2": lap.duration_sector_2,
                "duration_sector_3": lap.duration_sector_3,
            }

    return list(fastest.values())


# --------------------------------------------------
# Top Speeds
# --------------------------------------------------

def get_top_speeds(
    db: Session,
    session_key: int,
):
    rows = (
        db.query(
            Driver.driver_number,
            Driver.full_name,
            Driver.team_name,
            func.max(CarData.speed).label("top_speed"),
        )
        .join(
            CarData,
            (Driver.session_key == CarData.session_key)
            & (Driver.driver_number == CarData.driver_number),
        )
        .filter(
            Driver.session_key == session_key,
        )
        .group_by(
            Driver.driver_number,
            Driver.full_name,
            Driver.team_name,
        )
        .order_by(
            func.max(CarData.speed).desc(),
        )
        .all()
    )

    return [
        {
            "driver_number": row.driver_number,
            "driver_name": row.full_name,
            "team_name": row.team_name,
            "top_speed": float(row.top_speed)
            if row.top_speed is not None
            else None,
        }
        for row in rows
    ]

# --------------------------------------------------
# Driver Summary
# --------------------------------------------------

def get_driver_summary(
    db: Session,
    session_key: int,
    driver_number: int,
):
    driver = (
        db.query(Driver)
        .filter(
            Driver.session_key == session_key,
            Driver.driver_number == driver_number,
        )
        .first()
    )

    if driver is None:
        return None

    fastest_lap = (
        db.query(func.min(Lap.lap_duration))
        .filter(
            Lap.session_key == session_key,
            Lap.driver_number == driver_number,
        )
        .scalar()
    )

    telemetry = (
        db.query(
            func.max(CarData.speed),
            func.avg(CarData.speed),
            func.avg(CarData.rpm),
            func.avg(CarData.throttle),
            func.avg(CarData.brake),
            func.avg(CarData.drs),
        )
        .filter(
            CarData.session_key == session_key,
            CarData.driver_number == driver_number,
        )
        .first()
    )

    return {
        "driver_number": driver.driver_number,
        "driver_name": driver.full_name,
        "team_name": driver.team_name,

        "fastest_lap": (
            float(fastest_lap)
            if fastest_lap is not None
            else None
        ),

        "top_speed": (
            float(telemetry[0])
            if telemetry[0] is not None
            else None
        ),

        "average_speed": (
            round(float(telemetry[1]), 2)
            if telemetry[1] is not None
            else None
        ),

        "average_rpm": (
            round(float(telemetry[2]), 2)
            if telemetry[2] is not None
            else None
        ),

        "average_throttle": (
            round(float(telemetry[3]), 2)
            if telemetry[3] is not None
            else None
        ),

        "average_brake": (
            round(float(telemetry[4]), 2)
            if telemetry[4] is not None
            else None
        ),

        "drs_usage": (
            round(float(telemetry[5]), 2)
            if telemetry[5] is not None
            else None
        ),
    }


# --------------------------------------------------
# Driver Comparison
# --------------------------------------------------

def compare_drivers(
    db: Session,
    session_key: int,
    driver1: int,
    driver2: int,
):
    return {
        "driver_1": get_driver_summary(
            db,
            session_key,
            driver1,
        ),
        "driver_2": get_driver_summary(
            db,
            session_key,
            driver2,
        ),
    }

# --------------------------------------------------
# Race Summary
# --------------------------------------------------

def get_race_summary(
    db: Session,
    session_key: int,
):
    fastest = (
        db.query(
            Driver.full_name.label("driver_name"),
            Lap.lap_duration,
        )
        .join(
            Lap,
            (Driver.session_key == Lap.session_key)
            & (Driver.driver_number == Lap.driver_number),
        )
        .filter(
            Driver.session_key == session_key,
            Lap.lap_duration.isnot(None),
        )
        .order_by(
            Lap.lap_duration.asc(),
        )
        .first()
    )

    top_speed = (
        db.query(
            Driver.full_name.label("driver_name"),
            func.max(CarData.speed).label("top_speed"),
        )
        .join(
            CarData,
            (Driver.session_key == CarData.session_key)
            & (Driver.driver_number == CarData.driver_number),
        )
        .filter(
            Driver.session_key == session_key,
        )
        .group_by(
            Driver.full_name,
        )
        .order_by(
            func.max(CarData.speed).desc(),
        )
        .first()
    )

    weather = (
        db.query(
            func.avg(Weather.air_temperature),
            func.avg(Weather.track_temperature),
            func.avg(Weather.humidity),
            func.avg(Weather.wind_speed),
        )
        .filter(
            Weather.session_key == session_key,
        )
        .first()
    )

    yellow_flags = (
        db.query(func.count())
        .filter(
            RaceControl.session_key == session_key,
            RaceControl.flag == "YELLOW",
        )
        .scalar()
    )

    red_flags = (
        db.query(func.count())
        .filter(
            RaceControl.session_key == session_key,
            RaceControl.flag == "RED",
        )
        .scalar()
    )

    green_flags = (
        db.query(func.count())
        .filter(
            RaceControl.session_key == session_key,
            RaceControl.flag == "GREEN",
        )
        .scalar()
    )

    safety_car_events = (
        db.query(func.count())
        .filter(
            RaceControl.session_key == session_key,
            RaceControl.message.ilike("%SAFETY CAR%"),
        )
        .scalar()
    )

    return {
        "session_key": session_key,

        "fastest_lap_driver": (
            fastest.driver_name
            if fastest
            else None
        ),

        "fastest_lap": (
            float(fastest.lap_duration)
            if fastest and fastest.lap_duration is not None
            else None
        ),

        "highest_top_speed_driver": (
            top_speed.driver_name
            if top_speed
            else None
        ),

        "highest_top_speed": (
            float(top_speed.top_speed)
            if top_speed and top_speed.top_speed is not None
            else None
        ),

        "average_air_temperature": (
            round(float(weather[0]), 2)
            if weather and weather[0] is not None
            else None
        ),

        "average_track_temperature": (
            round(float(weather[1]), 2)
            if weather and weather[1] is not None
            else None
        ),

        "average_humidity": (
            round(float(weather[2]), 2)
            if weather and weather[2] is not None
            else None
        ),

        "average_wind_speed": (
            round(float(weather[3]), 2)
            if weather and weather[3] is not None
            else None
        ),

        "yellow_flags": yellow_flags,
        "red_flags": red_flags,
        "green_flags": green_flags,
        "safety_car_events": safety_car_events,
    }

# --------------------------------------------------
# Driver Performance Score
# --------------------------------------------------

def get_driver_performance_scores(
    db: Session,
    session_key: int,
):
    # ---------------------------------
    # Get all drivers
    # ---------------------------------

    drivers = (
        db.query(Driver)
        .filter(
            Driver.session_key == session_key,
        )
        .all()
    )

    summaries = []

    for driver in drivers:
        summary = get_driver_summary(
            db,
            session_key,
            driver.driver_number,
        )

        if summary is not None:
            summaries.append(summary)

    if not summaries:
        return []

    # ---------------------------------
    # Collect metric ranges
    # ---------------------------------

    fastest_laps = [
        float(s["fastest_lap"])
        for s in summaries
        if s["fastest_lap"] is not None
    ]

    top_speeds = [
        float(s["top_speed"])
        for s in summaries
        if s["top_speed"] is not None
    ]

    average_speeds = [
        float(s["average_speed"])
        for s in summaries
        if s["average_speed"] is not None
    ]

    throttles = [
        float(s["average_throttle"])
        for s in summaries
        if s["average_throttle"] is not None
    ]

    brakes = [
        float(s["average_brake"])
        for s in summaries
        if s["average_brake"] is not None
    ]

    drs_values = [
        float(s["drs_usage"])
        for s in summaries
        if s["drs_usage"] is not None
    ]

    # ---------------------------------
    # Normalization Helper
    # ---------------------------------

    def normalize(
        value,
        minimum,
        maximum,
        reverse=False,
    ):
        if value is None:
            return 0.0

        value = float(value)
        minimum = float(minimum)
        maximum = float(maximum)

        if maximum == minimum:
            return 100.0

        score = (
            (value - minimum)
            / (maximum - minimum)
        ) * 100.0

        if reverse:
            score = 100.0 - score

        return round(score, 2)

    results = []

    # ---------------------------------
    # Calculate Scores
    # ---------------------------------

    for summary in summaries:

        lap_score = normalize(
            summary["fastest_lap"],
            min(fastest_laps),
            max(fastest_laps),
            reverse=True,
        )

        speed_score = normalize(
            summary["top_speed"],
            min(top_speeds),
            max(top_speeds),
        )

        avg_speed_score = normalize(
            summary["average_speed"],
            min(average_speeds),
            max(average_speeds),
        )

        throttle_score = normalize(
            summary["average_throttle"],
            min(throttles),
            max(throttles),
        )

        brake_score = normalize(
            summary["average_brake"],
            min(brakes),
            max(brakes),
            reverse=True,
        )

        drs_score = normalize(
            summary["drs_usage"],
            min(drs_values),
            max(drs_values),
        )

        # ---------------------------------
        # Weighted Performance Score
        # ---------------------------------

        performance_score = (
            (lap_score * 0.35)
            + (speed_score * 0.25)
            + (avg_speed_score * 0.20)
            + (throttle_score * 0.10)
            + (brake_score * 0.05)
            + (drs_score * 0.05)
        )

        results.append(
            {
                "driver_number": summary["driver_number"],
                "driver_name": summary["driver_name"],
                "team_name": summary["team_name"],

                "lap_score": round(lap_score, 2),
                "speed_score": round(speed_score, 2),
                "average_speed_score": round(avg_speed_score, 2),
                "throttle_score": round(throttle_score, 2),
                "brake_score": round(brake_score, 2),
                "drs_score": round(drs_score, 2),

                "performance_score": round(
                    performance_score,
                    2,
                ),
            }
        )

    # ---------------------------------
    # Sort by Performance Score
    # ---------------------------------

    results.sort(
        key=lambda driver: driver["performance_score"],
        reverse=True,
    )

    # ---------------------------------
    # Assign Rank
    # ---------------------------------

    for rank, driver in enumerate(
        results,
        start=1,
    ):
        driver["rank"] = rank

    return results