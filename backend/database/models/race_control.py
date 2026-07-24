from datetime import datetime
from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from database.base import Base

if TYPE_CHECKING:
    from .session import Session


class RaceControl(Base):
    __tablename__ = "race_control"

    session_key: Mapped[int] = mapped_column(
        ForeignKey("sessions.session_key"),
        primary_key=True,
    )

    date: Mapped[datetime] = mapped_column(primary_key=True)

    category: Mapped[str | None]

    flag: Mapped[str | None]

    message: Mapped[str | None]

    scope: Mapped[str | None]

    sector: Mapped[int | None]

    driver_number: Mapped[int | None]

    lap_number: Mapped[int | None]

    session: Mapped["Session"] = relationship(
        back_populates="race_control"
    )