from app.services.telemetry_service import get_driver_telemetry

data = get_driver_telemetry(
    year=2024,
    grand_prix="Monaco",
    session_type="Q",
    driver="VER",
)

print(data.keys())
print(len(data["distance"]))
print(data["speed"][:10])