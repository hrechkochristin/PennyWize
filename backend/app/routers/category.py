from fastapi import APIRouter, Depends

from backend.app.crud.category import create_category, delete_category_by_id, update_category_by_id, \
    read_category_by_id, read_category, delete_category
from backend.app.crud.user import get_current_user
from backend.app.models import UserModel
from backend.app.schemas.category import CategoryAddSchema, CategorySchema
from backend.app.core.database import SessionDep

router = APIRouter(prefix="/categories", tags=["Categories"])
# Creating custom user's category
@router.post("", response_model=CategorySchema)
async def add_category(data: CategoryAddSchema, session: SessionDep, current_user: UserModel = Depends(get_current_user)):
    return await create_category(session, current_user.id, data)

# Reading all user's categories including custom and default
@router.get("", response_model=list[CategorySchema])
async def get_category(session: SessionDep, current_user: UserModel = Depends(get_current_user)):
    return await read_category(session, current_user.id)

# Deleting all user's custom categories
@router.delete("", response_model=bool)
async def remove_category(session: SessionDep, current_user: UserModel = Depends(get_current_user)):
    return await delete_category(session, current_user.id)

# Reading user's category by id (if category doesn't belong to user it's invisible)
@router.get("/{category_id}", response_model=CategorySchema)
async def get_category_by_id(category_id: int, session: SessionDep, current_user: UserModel = Depends(get_current_user)):
    return await read_category_by_id(session, category_id, current_user.id)


# Updating user's category attributes by id (if category doesn't belong to user it's invisible)
@router.patch("/{category_id}", response_model=CategorySchema)
async def renew_category_by_id(category_id: int, component_name: str, new_data: str, session: SessionDep, current_user: UserModel = Depends(get_current_user)):
    return await update_category_by_id(session, category_id, current_user.id, component_name, new_data)


# Deleting user's category by id (if category doesn't belong to user it's invisible)
@router.delete("/{category_id}", response_model=bool)
async def remove_category_by_id(category_id: int, session: SessionDep, current_user: UserModel = Depends(get_current_user)):
    return await delete_category_by_id(session, category_id, current_user.id)
