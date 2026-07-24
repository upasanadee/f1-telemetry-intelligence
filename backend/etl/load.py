from database.connection import SessionLocal
from database.models import Meeting, Session, Driver


def load_meetings(meetings):

    db = SessionLocal()

    try:

        for meeting in meetings:

            # Skip if already exists
            if db.get(Meeting, meeting["meeting_key"]):
                continue

            db.add(
                Meeting(
                    meeting_key=meeting["meeting_key"],
                    meeting_name=meeting["meeting_name"],
                    country_name=meeting["country_name"],
                    location=meeting["location"],
                    circuit_key=meeting["circuit_key"],
                    year=meeting["year"],
                )
            )

        db.commit()

    except Exception:
        db.rollback()
        raise

    finally:
        db.close()


def load_sessions(sessions):

    db = SessionLocal()

    try:

        for session in sessions:

            # Skip if already exists
            if db.get(Session, session["session_key"]):
                continue

            db.add(
                Session(
                    session_key=session["session_key"],
                    meeting_key=session["meeting_key"],
                    session_name=session["session_name"],
                    session_type=session["session_type"],
                    date_start=session["date_start"],
                    date_end=session["date_end"],
                )
            )

        db.commit()

    except Exception:
        db.rollback()
        raise

    finally:
        db.close()


def load_drivers(drivers):

    db = SessionLocal()

    try:

        for driver in drivers:

            # Skip if already exists
            if db.get(
                Driver,
                (
                    driver["session_key"],
                    driver["driver_number"],
                ),
            ):
                continue

            db.add(
                Driver(
                    session_key=driver["session_key"],
                    driver_number=driver["driver_number"],
                    meeting_key=driver["meeting_key"],
                    full_name=driver["full_name"],
                    name_acronym=driver["name_acronym"],
                    team_name=driver["team_name"],
                    team_colour=driver["team_colour"],
                    country_code=driver["country_code"],
                )
            )

        db.commit()

    except Exception:
        db.rollback()
        raise

    finally:
        db.close()