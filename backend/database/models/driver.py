from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from database.base import Base

if TYPE_CHECKING:
    from .session import Session
    from .lap import Lap
    from .car_data import CarData
    from .position import Position
    from .team_radio import TeamRadio


class Driver(Base):
    __tablename__ = "drivers"

    session_key: Mapped[int] = mapped_column(
        ForeignKey("sessions.session_key"),
        primary_key=True,
    )

    driver_number: Mapped[int] = mapped_column(
        primary_key=True,
    )

    full_name: Mapped[str]

    name_acronym: Mapped[str]

    team_name: Mapped[str]

    team_colour: Mapped[str]

    country_code: Mapped[str]

    session: Mapped["Session"] = relationship(
        back_populates="drivers"
    )

    laps: Mapped[list["Lap"]] = relationship(
        back_populates="driver",
        cascade="all, delete-orphan",
    )

    car_data: Mapped[list["CarData"]] = relationship(
        back_populates="driver",
        cascade="all, delete-orphan",
    )

    positions: Mapped[list["Position"]] = relationship(
        back_populates="driver",
        cascade="all, delete-orphan",
    )

    team_radio: Mapped[list["TeamRadio"]] = relationship(
        back_populates="driver",
        cascade="all, delete-orphan",
    )