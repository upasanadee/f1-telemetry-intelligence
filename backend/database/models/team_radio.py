from datetime import datetime
from typing import TYPE_CHECKING

from sqlalchemy import ForeignKeyConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship

from database.base import Base

if TYPE_CHECKING:
    from .driver import Driver


class TeamRadio(Base):
    __tablename__ = "team_radio"

    session_key: Mapped[int] = mapped_column(primary_key=True)

    driver_number: Mapped[int] = mapped_column(primary_key=True)

    date: Mapped[datetime] = mapped_column(primary_key=True)

    recording_url: Mapped[str]

    __table_args__ = (
        ForeignKeyConstraint(
            ["session_key", "driver_number"],
            ["drivers.session_key", "drivers.driver_number"],
        ),
    )

    driver: Mapped["Driver"] = relationship(
        back_populates="team_radio"
    )