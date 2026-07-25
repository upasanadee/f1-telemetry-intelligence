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


class DriverSummaryResponse(BaseModel):
    driver_number: int
    driver_name: str
    team_name: str

    fastest_lap: float | None = None
    top_speed: int | None = None

    average_speed: float | None = None
    average_rpm: float | None = None
    average_throttle: float | None = None
    average_brake: float | None = None
    drs_usage: float | None = None


class DriverComparisonResponse(BaseModel):
    driver_1: DriverSummaryResponse
    driver_2: DriverSummaryResponse


class RaceSummaryResponse(BaseModel):
    session_key: int

    fastest_lap_driver: str | None = None
    fastest_lap: float | None = None

    highest_top_speed_driver: str | None = None
    highest_top_speed: int | None = None

    average_air_temperature: float | None = None
    average_track_temperature: float | None = None
    average_humidity: float | None = None
    average_wind_speed: float | None = None

    yellow_flags: int
    red_flags: int
    green_flags: int
    safety_car_events: int

class PerformanceScoreResponse(BaseModel):
    rank: int

    driver_number: int
    driver_name: str
    team_name: str

    lap_score: float
    speed_score: float
    average_speed_score: float
    throttle_score: float
    brake_score: float
    drs_score: float

    performance_score: float