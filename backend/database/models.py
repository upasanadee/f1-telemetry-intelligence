from sqlalchemy import ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class Base(DeclarativeBase):
    pass


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


class Session(Base):
    __tablename__ = "sessions"

    session_key: Mapped[int] = mapped_column(
        primary_key=True,
        autoincrement=False,
    )

    meeting_key: Mapped[int] = mapped_column(
        ForeignKey("meetings.meeting_key"),
        nullable=False,
    )

    session_name: Mapped[str]
    session_type: Mapped[str]
    date_start: Mapped[str]
    date_end: Mapped[str]

    meeting: Mapped["Meeting"] = relationship(
        back_populates="sessions"
    )

    drivers: Mapped[list["Driver"]] = relationship(
        back_populates="session",
        cascade="all, delete-orphan",
    )


class Driver(Base):
    __tablename__ = "drivers"

    session_key: Mapped[int] = mapped_column(
        ForeignKey("sessions.session_key"),
        primary_key=True,
    )

    driver_number: Mapped[int] = mapped_column(
        primary_key=True
    )

    meeting_key: Mapped[int] = mapped_column(
        ForeignKey("meetings.meeting_key"),
        nullable=False,
    )

    full_name: Mapped[str]
    name_acronym: Mapped[str]
    team_name: Mapped[str]
    team_colour: Mapped[str]
    country_code: Mapped[str]

    session: Mapped["Session"] = relationship(
        back_populates="drivers"
    )