from __future__ import annotations
from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from backend.app.models.base import Base

class CategoryModel(Base):
    __tablename__ = "categories"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50), nullable=False)
    description: Mapped[str | None]
    icon: Mapped[str | None]
    color: Mapped[str] = mapped_column(String(20), nullable=False)

    user_id: Mapped[int | None] = mapped_column(
        ForeignKey("users.id"),
        nullable=True
    )
    user: Mapped["UserModel | None"] = relationship(
        back_populates="categories"
    )

    transactions: Mapped[list["TransactionModel"]] = relationship(
        back_populates="category"
    )