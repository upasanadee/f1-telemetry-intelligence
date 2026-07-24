from typing import TYPE_CHECKING

from sqlalchemy.orm import Mapped, mapped_column, relationship

from database.base import Base

if TYPE_CHECKING:
    from .session import Session


class Meeting(Base):
    __tablename__ = "meetings"

    meeting_key: Mapped[int] = mapped_column(
        primary_key=True,
        autoincrement=False,
    )

    meeting_name: Mapped[str]

    country_name: Mapped[str]

    location: Mapped[str]

    circuit_key: Mapped[int]

    year: Mapped[int]

    sessions: Mapped[list["Session"]] = relationship(
        back_populates="meeting",
        cascade="all, delete-orphan",
    )