from fastapi import APIRouter

from backend.app.crud.user import create_user, read_user, read_user_by_id, update_user_by_id

from backend.app.core.database import SessionDep
from backend.app.schemas.user import UserAddSchema, UserSchema

router = APIRouter(prefix="/users", tags=["Users"])


@router.post("/create", response_model=UserSchema)
async def add_user(data: UserAddSchema, session: SessionDep):
    return await create_user(session, data)

@router.get("/read_all", response_model=list[UserSchema])
async def get_user(session: SessionDep):
    return await read_user(session)

@router.get("/read_by_id", response_model=UserSchema)
async def get_user_by_id(session: SessionDep, user_id: int):
    return await read_user_by_id(session, user_id)

@router.patch("/update_by_id", response_model=UserSchema)
async def renew_user_by_id(session: SessionDep, user_id: int, component_name: str, new_data: str):
    return await update_user_by_id(session, user_id, component_name, new_data)

# @router.post("/delete_by_id", response_model=bool)
# async def remove_user_by_id(session: SessionDep, user_id: int):
#     return await delete_user_by_id(session, user_id, user_id)
#
# @router.post("/delete_all", response_model=bool)
# async def remove_user(session: SessionDep, user_id: int):
#     return await delete_user(session, user_id)