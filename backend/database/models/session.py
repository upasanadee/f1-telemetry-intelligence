from datetime import datetime
from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from database.base import Base

if TYPE_CHECKING:
    from .driver import Driver
    from .meeting import Meeting
    from .weather import Weather
    from .race_control import RaceControl


class Session(Base):
    __tablename__ = "sessions"

    session_key: Mapped[int] = mapped_column(
        primary_key=True,
        autoincrement=False,
    )

    meeting_key: Mapped[int] = mapped_column(
        ForeignKey("meetings.meeting_key"),
        nullable=False,
        index=True,
    )

    session_name: Mapped[str]

    session_type: Mapped[str]

    date_start: Mapped[datetime]

    date_end: Mapped[datetime]

    meeting: Mapped["Meeting"] = relationship(
        back_populates="sessions"
    )

    drivers: Mapped[list["Driver"]] = relationship(
        back_populates="session",
        cascade="all, delete-orphan",
    )

    weather: Mapped[list["Weather"]] = relationship(
        back_populates="session",
        cascade="all, delete-orphan",
    )

    race_control: Mapped[list["RaceControl"]] = relationship(
        back_populates="session",
        cascade="all, delete-orphan",
    )