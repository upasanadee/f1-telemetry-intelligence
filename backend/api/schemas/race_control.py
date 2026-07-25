from datetime import datetime

from pydantic import BaseModel, ConfigDict


class RaceControlResponse(BaseModel):
    session_key: int
    date: datetime

    category: str | None = None
    flag: str | None = None
    message: str | None = None
    scope: str | None = None

    sector: int | None = None
    driver_number: int | None = None
    lap_number: int | None = None

    model_config = ConfigDict(from_attributes=True)