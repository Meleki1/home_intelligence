from sqlalchemy import String, ForeignKey, Float
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.database.base import Base
from app.database.mixins import TimeStampMixin, UUIDMixin, SoftDeleteMixin



class HomeState(UUIDMixin, TimeStampMixin,Base):


    __tablename__ = "home_state"

    home_id: Mapped[str] = mapped_column(
        ForeignKey("homes.id"),
        nullable=False
    )

    risk_level: Mapped[str] = mapped_column(
        String(50),
        default="low",
        nullable=False
    )

    health_score: Mapped[float] = mapped_column(
        Float,
        default=100.0,
        nullable=False
    )