from __future__ import annotations
from sqlalchemy.orm import Mapped, mapped_column, relationship

from backend.app.models.base import Base

DEFAULT_CATEGORIES = [
    "Food",
    "Transport",
    "Shopping",
    "Health",
    "Entertainment",
    "Salary",
]

class UserModel(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)

    username: Mapped[str]
    email: Mapped[str]
    password_hash: Mapped[str]

    categories: Mapped[list["CategoryModel"]] = relationship(
        back_populates="user"
    )

    transactions: Mapped[list["TransactionModel"]] = relationship(
        back_populates="user"
    )