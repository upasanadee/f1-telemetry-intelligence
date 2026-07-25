from datetime import datetime

from pydantic import BaseModel, ConfigDict


class LapResponse(BaseModel):
    session_key: int
    driver_number: int
    lap_number: int

    date_start: datetime | None = None

    lap_duration: float | None = None

    duration_sector_1: float | None = None
    duration_sector_2: float | None = None
    duration_sector_3: float | None = None

    stint: int | None = None

    is_pit_out_lap: bool | None = None

    model_config = ConfigDict(from_attributes=True)