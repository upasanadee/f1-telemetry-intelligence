from datetime import datetime

from pydantic import BaseModel, ConfigDict


class PositionResponse(BaseModel):
    session_key: int
    driver_number: int
    date: datetime

    x: float | None = None
    y: float | None = None
    z: float | None = None

    model_config = ConfigDict(from_attributes=True)