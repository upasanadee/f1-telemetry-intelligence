import logging
import fastf1
from pathlib import Path

# Enable debug logging
logging.basicConfig(level=logging.DEBUG)

cache_dir = Path("backend/cache")
cache_dir.mkdir(parents=True, exist_ok=True)

fastf1.Cache.enable_cache(str(cache_dir))

session = fastf1.get_session(2024, "Monaco", "Q")

print("Loading session...")

try:
    session.load()
    print("Session loaded")
except Exception as e:
    print("LOAD FAILED")
    raise

print("\nTrying to access laps...\n")

try:
    print(session.laps.head())
except Exception as e:
    print(type(e).__name__)
    print(e)