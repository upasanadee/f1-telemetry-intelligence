from fastapi import FastAPI

from api.routes.meetings import router as meetings_router

app = FastAPI(
    title="F1 Telemetry Intelligence API",
    description="Backend API for Formula 1 telemetry analytics",
    version="1.0.0",
)

app.include_router(meetings_router)


@app.get("/")
def root():
    return {
        "status": "running",
        "message": "Welcome to the F1 Telemetry Intelligence API"
    }