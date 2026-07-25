from datetime import datetime

from pydantic import BaseModel, ConfigDict


class WeatherResponse(BaseModel):
    session_key: int
    date: datetime

    air_temperature: float | None = None
    track_temperature: float | None = None
    humidity: float | None = None
    pressure: float | None = None
    rainfall: bool | None = None
    wind_direction: int | None = None
    wind_speed: float | None = None

    model_config = ConfigDict(from_attributes=True)