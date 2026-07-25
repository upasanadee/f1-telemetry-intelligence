from datetime import datetime

from pydantic import BaseModel, ConfigDict


class SessionResponse(BaseModel):
    session_key: int
    meeting_key: int
    session_name: str
    session_type: str
    date_start: datetime | None = None
    date_end: datetime | None = None

    model_config = ConfigDict(from_attributes=True)