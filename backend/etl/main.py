from etl.extract import (
    extract_meetings,
    extract_sessions,
    extract_drivers,
)

from etl.load import (
    load_meetings,
    load_sessions,
    load_drivers,
)


def main():

    print("Extracting meetings...")

    meetings = extract_meetings(2024)

    print(f"Found {len(meetings)} meetings")

    load_meetings(meetings)

    print("Meetings loaded.")

    total_sessions = 0
    total_drivers = 0

    for meeting in meetings:

        sessions = extract_sessions(
            meeting["meeting_key"]
        )

        load_sessions(sessions)

        total_sessions += len(sessions)

        print(
            f"Loaded {len(sessions)} sessions for "
            f"{meeting['meeting_name']}"
        )

        for session in sessions:

            drivers = extract_drivers(
                session["session_key"]
            )

            load_drivers(drivers)

            total_drivers += len(drivers)

            print(
                f"    Loaded {len(drivers)} drivers "
                f"for {session['session_name']}"
            )

    print("\nPipeline completed!")
    print(f"Meetings : {len(meetings)}")
    print(f"Sessions : {total_sessions}")
    print(f"Drivers : {total_drivers}")


if __name__ == "__main__":
    main()