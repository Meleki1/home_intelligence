from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.database.base import Base
from app.database.mixins import TimeStampMixin, UUIDMixin, SoftDeleteMixin



class HomeInformation(
    UUIDMixin, 
    TimeStampMixin,
    Base
):


    __tablename__ = "home_information"


    home_id: Mapped[str] = mapped_column(
        ForeignKey("homes.id"),
        nullable=False
    )

    country: Mapped[str] = mapped_column(
        String(100),
        nullable=False
    )

    city: Mapped[str] = mapped_column(
        String(100),
        nullable=False
    )

    address: Mapped[str] = mapped_column(
        String(255),
        nullable=False
    )

    Zipcode: Mapped[str | None] = mapped_column(
        String(50),
        nullable=True
    )

    home = relationship(
        "Home",
        back_populates="information"
    )

