from etl.extract import (
    extract_meetings,
    extract_sessions,
    extract_drivers,
    extract_laps,
    extract_car_data,
    extract_positions,
    extract_weather,
    extract_race_control,
    extract_team_radio,
)

from etl.transform import (
    transform_meetings,
    transform_sessions,
    transform_drivers,
    transform_laps,
    transform_car_data,
    transform_positions,
    transform_weather,
    transform_race_control,
    transform_team_radio,
)

from etl.load import bulk_load

from database.models import (
    Meeting,
    Session,
    Driver,
    Lap,
    CarData,
    Position,
    Weather,
    RaceControl,
    TeamRadio,
)


def process_dataset(
    name: str,
    model,
    extractor,
    transformer,
    *args,
) -> int:
    """
    Extract -> Transform -> Load helper.
    Returns the number of loaded records.
    """

    print(f"    Fetching {name}...")

    records = transformer(
        extractor(*args)
    )

    print(f"    Retrieved {len(records)} {name}")

    if records:
        bulk_load(
            model,
            records,
        )

        print(f"    {name.capitalize()} loaded.")

    return len(records)


def run_pipeline(year: int):

    print(f"\n========== OpenF1 ETL ({year}) ==========\n")

    meetings = transform_meetings(
        extract_meetings(year)
    )

    bulk_load(
        Meeting,
        meetings,
    )

    totals = {
        "meetings": len(meetings),
        "sessions": 0,
        "drivers": 0,
        "laps": 0,
        "car_data": 0,
        "positions": 0,
        "weather": 0,
        "race_control": 0,
        "team_radio": 0,
    }

    for meeting in meetings:

        meeting_key = meeting["meeting_key"]

        print("\n" + "=" * 60)
        print(f"Meeting {meeting_key}")
        print("=" * 60)

        sessions = transform_sessions(
            extract_sessions(meeting_key)
        )

        bulk_load(
            Session,
            sessions,
        )

        totals["sessions"] += len(sessions)

        for session in sessions:

            session_key = session["session_key"]

            print(f"\nSession {session_key}")

            drivers = transform_drivers(
                extract_drivers(session_key)
            )

            bulk_load(
                Driver,
                drivers,
            )

            totals["drivers"] += len(drivers)

            # -----------------------------
            # Session-level endpoints
            # -----------------------------

            totals["weather"] += process_dataset(
                "weather",
                Weather,
                extract_weather,
                transform_weather,
                session_key,
            )

            totals["race_control"] += process_dataset(
                "race control",
                RaceControl,
                extract_race_control,
                transform_race_control,
                session_key,
            )

            totals["positions"] += process_dataset(
                "positions",
                Position,
                extract_positions,
                transform_positions,
                session_key,
            )

            # -----------------------------
            # Driver-level endpoints
            # -----------------------------

            for driver in drivers:

                driver_number = driver["driver_number"]

                print(f"\nDriver {driver_number}")

                try:

                    totals["laps"] += process_dataset(
                        "laps",
                        Lap,
                        extract_laps,
                        transform_laps,
                        session_key,
                        driver_number,
                    )

                    totals["car_data"] += process_dataset(
                        "car data",
                        CarData,
                        extract_car_data,
                        transform_car_data,
                        session_key,
                        driver_number,
                    )

                    totals["team_radio"] += process_dataset(
                        "team radio",
                        TeamRadio,
                        extract_team_radio,
                        transform_team_radio,
                        session_key,
                        driver_number,
                    )

                except Exception as e:

                    print(
                        f"\nERROR: Session {session_key}, "
                        f"Driver {driver_number}"
                    )

                    print(e)

                    continue

    print("\n" + "=" * 60)
    print("ETL COMPLETE")
    print("=" * 60)

    for key, value in totals.items():
        print(f"{key.replace('_', ' ').title():15}: {value}")