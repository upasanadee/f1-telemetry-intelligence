from pydantic import BaseModel, ConfigDict


class DriverResponse(BaseModel):
    session_key: int
    driver_number: int
    full_name: str
    name_acronym: str
    team_name: str
    team_colour: str
    country_code: str

    model_config = ConfigDict(from_attributes=True)