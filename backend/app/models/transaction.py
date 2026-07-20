from __future__ import annotations
from datetime import datetime

from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import mapped_column, Mapped, relationship

from backend.app.models.base import Base


class TransactionModel(Base):
    __tablename__ = "transactions"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    description: Mapped[str | None]
    amount: Mapped[float] = mapped_column(nullable=False)
    type: Mapped[str] = mapped_column(String(20), default="expense", nullable=False)
    currency: Mapped[str] = mapped_column(String(3), default="UAH")
    account_name: Mapped[str | None]
    date: Mapped[datetime] = mapped_column(default=datetime.now)

    category_id: Mapped[int] = mapped_column(
        ForeignKey("categories.id")
    )

    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id")
    )

    category: Mapped["CategoryModel"] = relationship(
        back_populates="transactions"
    )

    user: Mapped["UserModel"] = relationship(
        back_populates="transactions"
    )
