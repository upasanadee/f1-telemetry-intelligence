from fastapi import FastAPI

from api.routes.meetings import router as meetings_router
from api.routes.sessions import router as sessions_router
from api.routes.drivers import router as drivers_router
from api.routes.laps import router as laps_router
from api.routes.car_data import router as car_data_router
from api.routes.positions import router as positions_router
from api.routes.weather import router as weather_router

app = FastAPI(
    title="F1 Telemetry Intelligence API",
    description="Backend API for Formula 1 telemetry analytics",
    version="1.0.0",
)

app.include_router(meetings_router)
app.include_router(sessions_router)
app.include_router(drivers_router)
app.include_router(laps_router)
app.include_router(car_data_router)
app.include_router(positions_router)
app.include_router(weather_router)

@app.get("/")
def root():
    return {
        "status": "running",
        "message": "Welcome to the F1 Telemetry Intelligence API"
    }