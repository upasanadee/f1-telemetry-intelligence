from datetime import datetime
from typing import TYPE_CHECKING

from sqlalchemy import Float, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from database.base import Base

if TYPE_CHECKING:
    from .session import Session


class Weather(Base):
    __tablename__ = "weather"

    session_key: Mapped[int] = mapped_column(
        ForeignKey("sessions.session_key"),
        primary_key=True,
    )

    date: Mapped[datetime] = mapped_column(primary_key=True)

    air_temperature: Mapped[float | None] = mapped_column(Float)

    track_temperature: Mapped[float | None] = mapped_column(Float)

    humidity: Mapped[float | None] = mapped_column(Float)

    pressure: Mapped[float | None] = mapped_column(Float)

    rainfall: Mapped[bool | None]

    wind_direction: Mapped[int | None]

    wind_speed: Mapped[float | None] = mapped_column(Float)

    session: Mapped["Session"] = relationship(
        back_populates="weather"
    )