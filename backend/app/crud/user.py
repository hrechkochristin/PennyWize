from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt

from sqlalchemy import select, insert
from sqlalchemy.ext.asyncio import AsyncSession

from backend.app.core.database import get_session
from backend.app.core.jwt import create_access_token, SECRET_KEY, ALGORITHM
from backend.app.core.password import verify_password, hash_password
from backend.app.models import UserModel

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="users/login")

async def get_current_user(
    token: str = Depends(oauth2_scheme),
    session: AsyncSession = Depends(get_session)
):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_id: str = payload.get("sub")

        if user_id is None:
            raise HTTPException(status_code=401, detail="Invalid token")

    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")

    result = await session.execute(
        select(UserModel).where(UserModel.id == int(user_id))
    )
    user = result.scalar_one_or_none()

    if user is None:
        raise HTTPException(status_code=401, detail="User not found")

    return user

async def signup_user(user_data, session):
    result = await session.execute(select(UserModel).where(UserModel.username == user_data.username))
    user = result.scalar_one_or_none()
    if user is not None:
        raise HTTPException(status_code=400, detail="Username already exists")

    result = await session.execute(select(UserModel).where(UserModel.email == user_data.email))
    email = result.scalar_one_or_none()
    if email is not None:
        raise HTTPException(status_code=400, detail="Email already exists")

    new_user = UserModel(username=user_data.username, email=user_data.email, password_hash=hash_password(user_data.password))
    session.add(new_user)
    await session.commit()
    await session.refresh(new_user)

    token = create_access_token({"sub": str(new_user.id)})

    return {"access_token": token, "token_type": "bearer"}

async def login_user(form_data, session):
    result = await session.execute(select(UserModel).where(UserModel.username == form_data.username))
    user = result.scalar_one_or_none()

    if user is None:
        raise HTTPException(status_code=401, detail="Incorrect username or password")

    if not verify_password(form_data.password, user.password_hash):
        raise HTTPException(status_code=401, detail="Incorrect username or password")

    token = create_access_token({"sub": str(user.id)})

    return {"access_token": token, "token_type": "bearer"}