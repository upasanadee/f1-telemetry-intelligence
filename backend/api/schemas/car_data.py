from datetime import datetime

from pydantic import BaseModel, ConfigDict


class CarDataResponse(BaseModel):
    session_key: int
    driver_number: int
    date: datetime

    speed: int | None = None
    rpm: int | None = None
    n_gear: int | None = None
    throttle: int | None = None
    brake: int | None = None
    drs: int | None = None

    model_config = ConfigDict(from_attributes=True)