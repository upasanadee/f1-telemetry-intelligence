from pydantic import BaseModel


class MeetingResponse(BaseModel):
    meeting_key: int
    country_name: str
    circuit_key: int
    meeting_name: str
    location: str
    year: int

    class Config:
        from_attributes = True