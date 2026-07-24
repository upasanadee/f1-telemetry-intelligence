from datetime import datetime
from typing import Any


def parse_datetime(value: str | None) -> datetime | None:
    """
    Safely converts an ISO-8601 timestamp into a Python datetime.
    Returns None if the value is missing or invalid.
    """

    if not value:
        return None

    try:
        return datetime.fromisoformat(
            value.replace("Z", "+00:00")
        )
    except ValueError:
        return None


def transform_meetings(
    records: list[dict[str, Any]],
) -> list[dict[str, Any]]:
    return records


def transform_sessions(
    records: list[dict[str, Any]],
) -> list[dict[str, Any]]:
    return records


def transform_drivers(
    records: list[dict[str, Any]],
) -> list[dict[str, Any]]:
    return records


def transform_laps(
    records: list[dict[str, Any]],
) -> list[dict[str, Any]]:
    return [
        {
            **record,
            "date_start": parse_datetime(
                record.get("date_start")
            ),
        }
        for record in records
    ]


def transform_car_data(
    records: list[dict[str, Any]],
) -> list[dict[str, Any]]:
    return [
        {
            **record,
            "date": parse_datetime(
                record.get("date")
            ),
        }
        for record in records
    ]


def transform_positions(
    records: list[dict[str, Any]],
) -> list[dict[str, Any]]:
    return [
        {
            **record,
            "date": parse_datetime(
                record.get("date")
            ),
        }
        for record in records
    ]


def transform_weather(
    records: list[dict[str, Any]],
) -> list[dict[str, Any]]:
    return [
        {
            **record,
            "date": parse_datetime(
                record.get("date")
            ),
        }
        for record in records
    ]


def transform_race_control(
    records: list[dict[str, Any]],
) -> list[dict[str, Any]]:
    return [
        {
            **record,
            "date": parse_datetime(
                record.get("date")
            ),
        }
        for record in records
    ]


def transform_team_radio(
    records: list[dict[str, Any]],
) -> list[dict[str, Any]]:
    return [
        {
            **record,
            "date": parse_datetime(
                record.get("date")
            ),
        }
        for record in records
    ]