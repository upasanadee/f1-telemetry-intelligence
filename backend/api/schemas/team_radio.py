from datetime import datetime

from pydantic import BaseModel, ConfigDict


class TeamRadioResponse(BaseModel):
    session_key: int
    driver_number: int
    date: datetime

    recording_url: str

    model_config = ConfigDict(from_attributes=True)