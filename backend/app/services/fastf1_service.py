import fastf1
from pathlib import Path

CACHE_DIR = Path(__file__).parent.parent.parent / "cache"

fastf1.Cache.enable_cache(str(CACHE_DIR))


def load_session(year, grand_prix, session_type):
    session = fastf1.get_session(
        year,
        grand_prix,
        session_type,
    )

    session.load()

    return session