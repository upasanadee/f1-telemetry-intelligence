from pathlib import Path

DATA_DIR = (
    Path(__file__).resolve().parent.parent.parent
    / "data"
    / "sessions"
)


def get_seasons():
    if not DATA_DIR.exists():
        return []

    return sorted(
        [
            folder.name
            for folder in DATA_DIR.iterdir()
            if folder.is_dir()
        ]
    )


def get_events(season: str):
    path = DATA_DIR / season

    if not path.exists():
        return []

    return sorted(
        [
            folder.name
            for folder in path.iterdir()
            if folder.is_dir()
        ]
    )


def get_sessions(season: str, event: str):
    path = DATA_DIR / season / event

    if not path.exists():
        return []

    return sorted(
        [
            folder.name
            for folder in path.iterdir()
            if folder.is_dir()
        ]
    )


def get_drivers(
    season: str,
    event: str,
    session: str,
):
    path = DATA_DIR / season / event / session

    if not path.exists():
        return []

    drivers = []

    for file in path.glob("*.json"):
        if file.stem != "metadata":
            drivers.append(file.stem)

    return sorted(drivers)