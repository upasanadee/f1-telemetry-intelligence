from datetime import datetime
from typing import TYPE_CHECKING

from sqlalchemy import Boolean, Float, ForeignKeyConstraint, Index
from sqlalchemy.orm import Mapped, mapped_column, relationship

from database.base import Base

if TYPE_CHECKING:
    from .driver import Driver


class Lap(Base):
    __tablename__ = "laps"

    session_key: Mapped[int] = mapped_column(primary_key=True)

    driver_number: Mapped[int] = mapped_column(primary_key=True)

    lap_number: Mapped[int] = mapped_column(primary_key=True)

    date_start: Mapped[datetime | None]

    lap_duration: Mapped[float | None] = mapped_column(Float)

    duration_sector_1: Mapped[float | None] = mapped_column(Float)

    duration_sector_2: Mapped[float | None] = mapped_column(Float)

    duration_sector_3: Mapped[float | None] = mapped_column(Float)

    stint: Mapped[int | None]

    is_pit_out_lap: Mapped[bool | None] = mapped_column(Boolean)

    __table_args__ = (
        ForeignKeyConstraint(
            ["session_key", "driver_number"],
            ["drivers.session_key", "drivers.driver_number"],
        ),
        Index("idx_laps_driver", "session_key", "driver_number"),
        Index("idx_laps_time", "session_key", "lap_number"),
    )

    driver: Mapped["Driver"] = relationship(
        back_populates="laps"
    )