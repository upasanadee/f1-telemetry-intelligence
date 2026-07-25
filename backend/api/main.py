from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api.routes.meetings import router as meetings_router
from api.routes.sessions import router as sessions_router
from api.routes.drivers import router as drivers_router
from api.routes.laps import router as laps_router
from api.routes.car_data import router as car_data_router
from api.routes.positions import router as positions_router
from api.routes.weather import router as weather_router
from api.routes.race_control import router as race_control_router
from api.routes.team_radio import router as team_radio_router
from api.routes.analytics import router as analytics_router

app = FastAPI(
    title="F1 Telemetry Intelligence API",
    description="Backend API for Formula 1 telemetry analytics",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
        "http://127.0.0.1:3000",
        "https://laughing-journey-5gpr9jxqqx5crq7-3000.app.github.dev",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(meetings_router)
app.include_router(sessions_router)
app.include_router(drivers_router)
app.include_router(laps_router)
app.include_router(car_data_router)
app.include_router(positions_router)
app.include_router(weather_router)
app.include_router(race_control_router)
app.include_router(team_radio_router)
app.include_router(analytics_router)


@app.get("/")
def root():
    return {
        "status": "running",
        "message": "Welcome to the F1 Telemetry Intelligence API",
    }