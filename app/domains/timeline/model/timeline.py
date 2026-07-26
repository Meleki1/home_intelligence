from uuid import UUID
from uuid import uuid4
from datetime import datetime, timezone
from sqlalchemy import String, DateTime
from sqlalchemy.orm import Mapped, mapped_column
from app.database.base import Base


class Timeline(Base):
    __tablename__ = "timelines"

    id:Mapped[UUID] = (
        mapped_column(
            primary_key=True,
            default=uuid4
        )
    )

    event_type:Mapped[str] = (
        mapped_column(
            String(50),
            nullable=False
        )
    )

    event_name:Mapped[str] = (
        mapped_column(
            String(100),
            nullable=False
        )
    )

    state:Mapped[str] = (
        mapped_column(
            String(50),
            nullable=False
        )
    )

    description:Mapped[str] = (
        mapped_column(
            String(255),
            nullable=False
        )
    )

    created_at:Mapped[datetime] = (
        mapped_column(
            DateTime(
                timezone=True
            ),
            
            default=lambda:
            datetime.now(
                timezone.utc
            )
        )
    )