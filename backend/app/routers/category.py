from fastapi import APIRouter

from backend.app.crud.category import create_category, delete_category_by_id, update_category_by_id, \
    read_category_by_id, read_category, delete_category
from backend.app.schemas.category import CategoryAddSchema, CategorySchema
from backend.app.core.database import SessionDep

router = APIRouter(prefix="/categories", tags=["Categories"])


@router.post("/create/{user_id}", response_model=CategorySchema)
async def add_category(user_id: int, data: CategoryAddSchema, session: SessionDep):
    return await create_category(session, user_id, data)


@router.get("/read_all/{user_id}", response_model=list[CategorySchema])
async def get_category(session: SessionDep, user_id: int):
    return await read_category(session, user_id)

@router.get("/read_by_id/{user_id}", response_model=CategorySchema)
async def get_category_by_id(session: SessionDep, category_id: int, user_id: int):
    return await read_category_by_id(session, category_id, user_id)

@router.patch("/update_by_id/{user_id}", response_model=CategorySchema)
async def renew_category_by_id(session: SessionDep, category_id: int, user_id: int, component_name: str, new_data: str):
    return await update_category_by_id(session, category_id, user_id, component_name, new_data)

@router.post("/delete_by_id/{user_id}", response_model=bool)
async def remove_category_by_id(session: SessionDep, category_id: int, user_id: int):
    return await delete_category_by_id(session, category_id, user_id)

@router.post("/delete_all/{user_id}", response_model=bool)
async def remove_category(session: SessionDep, user_id: int):
    return await delete_category(session, user_id)