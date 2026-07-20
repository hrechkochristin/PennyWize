from fastapi import HTTPException
from sqlalchemy import select

from backend.app.models.user import UserModel
from backend.app.schemas.user import UserAddSchema

from pwdlib import PasswordHash

password_hash = PasswordHash.recommended()


def hash_password(password: str) -> str:
    return password_hash.hash(password)


def verify_password(password: str, hashed_password: str) -> bool:
    return password_hash.verify(password, hashed_password)

async def create_user(session, data: UserAddSchema):
    new_user = UserModel(
        username=data.username,
        email=data.email,
        password_hash=hash_password(data.password)
    )
    session.add(new_user)
    await session.commit()
    await session.refresh(new_user)
    return new_user

async def read_user(session):
    result = await session.execute(select(UserModel))
    return result.scalars().all()

async def read_user_by_id(session, user_id: int):
    result = await session.execute(select(UserModel).where(UserModel.id == user_id))
    return result.scalars().one_or_none()

ALLOWED_FIELDS = {
    "username",
    "email",
    "password"
}

async def update_user_by_id(session, user_id: int, component_name: str, new_data: str):
    result = await session.execute(select(UserModel).where(UserModel.id == user_id))
    user = result.scalars().one_or_none()

    if not user:
        return None

    if component_name not in ALLOWED_FIELDS:
        raise HTTPException(status_code=400, detail="Invalid field")

    setattr(user, component_name, new_data)

    await session.commit()
    await session.refresh(user)

    return user
