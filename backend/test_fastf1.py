print("START")

from app.services.fastf1_service import load_session

print("IMPORT OK")

session = load_session(
    2024,
    "Monaco",
    "Q",
)

print("LOAD RETURNED")

print(session)