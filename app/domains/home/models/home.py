from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.database.base import Base
from app.database.mixins import TimeStampMixin, UUIDMixin, SoftDeleteMixin



class Home(
    UUIDMixin,
    TimeStampMixin,
    SoftDeleteMixin,
    Base
    ):

    __tablename__ = "homes"


    name: Mapped[str] = mapped_column(
        String(150),
        nullable=False
    )

    home_type: Mapped[str] = mapped_column(
        String(50),
        nullable=False
    )

    description: Mapped[str | None] = mapped_column(
        String(500),
        nullable=True
    )

    status: Mapped[str] = mapped_column(
        String(50),
        nullable=False
    )

    information = relationship(
        "HomeInformation",
        back_populates="home",
        uselist=False
    )

    state = relationship(
        "HomeState",
        uselist=False
    )
