import uuid

from sqlalchemy import UUID
from sqlalchemy.orm import Mapped, mapped_column

from db import Base


class StateModel(Base):
    __tablename__ = "states"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(), primary_key=True, default=uuid.uuid4()
    )
    name: Mapped[str]
    comment: Mapped[str]
