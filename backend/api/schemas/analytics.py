from pydantic import BaseModel


class FastestLapResponse(BaseModel):
    driver_number: int
    driver_name: str
    team_name: str

    lap_number: int
    lap_duration: float

    duration_sector_1: float | None = None
    duration_sector_2: float | None = None
    duration_sector_3: float | None = None


class TopSpeedResponse(BaseModel):
    driver_number: int
    driver_name: str
    team_name: str

    top_speed: int