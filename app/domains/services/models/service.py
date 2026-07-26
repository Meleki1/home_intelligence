from datetime import datetime, timezone
from uuid import UUID, uuid4
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column
from app.database.base import Base

class Service(Base):
    __tablename__="services"

    id:Mapped[UUID] = (
        mapped_column(
            primary_key=True,
            default=uuid4
        )
    )

    name:Mapped[str] = (
        mapped_column(
            String(255),
            nullable=False
        )
    )

    description:Mapped[str]=mapped_column(
        String(1000),
        nullable=False
    )

    category:Mapped[str]=mapped_column(
        String(255),
        nullable=False
    )

    state:Mapped[str]=mapped_column(
        String(50),
        nullable=False,
        default="ACTIVE"
    )

    created_at:Mapped[datetime]=mapped_column(
        default=lambda:
        datetime.now(
            timezone.utc
        )
    )