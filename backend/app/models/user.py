from enum import Enum

from sqlalchemy import Enum as SQLEnum
from sqlalchemy.orm import Mapped, mapped_column, relationship

from backend.app.models.base import Base


class UserRole(str, Enum):
    admin = "admin"
    developer = "developer"
    user = "user"


class UserModel(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)

    role: Mapped[UserRole] = mapped_column(
        SQLEnum(UserRole, name="userrole", create_type=True),
        default=UserRole.user,
        nullable=False,
    )

    username: Mapped[str]
    email: Mapped[str]
    password_hash: Mapped[str]

    categories: Mapped[list["CategoryModel"]] = relationship(
        back_populates="user"
    )

    transactions: Mapped[list["TransactionModel"]] = relationship(
        back_populates="user"
    )