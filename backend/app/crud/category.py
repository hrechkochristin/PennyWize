from fastapi import HTTPException
from sqlalchemy import select, delete

from backend.app.core.database import offset, limit
from backend.app.models import CategoryModel
from backend.app.schemas.category import CategoryAddSchema


async def create_category(session, user_id: int,  data: CategoryAddSchema):
    new_category = CategoryModel(
        name=data.name,
        description=data.description,
        icon=data.icon,
        color=data.color,
        user_id=user_id
    )
    session.add(new_category)
    await session.commit()
    await session.refresh(new_category)
    return new_category


async def read_category(session, user_id: int):
    result = await session.execute(select(CategoryModel).where(
    (CategoryModel.user_id == user_id) |
    (CategoryModel.user_id.is_(None)).limit(limit).offset(offset)
))
    return result.scalars().all()

async def delete_category(session, user_id: int):
    result = await session.execute(delete(CategoryModel).where(CategoryModel.user_id == user_id))
    await session.commit()

    return bool(result.rowcount)

async def read_category_by_id(session, category_id: int, user_id: int):
    result = await session.execute(select(CategoryModel).where(CategoryModel.id == category_id))
    category = result.scalars().one_or_none()

    if not category:
        return None

    if category.user_id != user_id and category.user_id is not None:
        raise HTTPException(status_code=403, detail="Access denied")

    return category

ALLOWED_FIELDS = {
    "name",
    "description",
    "icon",
    "color"
}

async def update_category_by_id(session, category_id: int, user_id: int, component_name: str, new_data: str):
    result = await session.execute(select(CategoryModel).where(CategoryModel.id == category_id))
    category = result.scalars().one_or_none()

    if not category:
        return None

    if category.user_id != user_id:
        raise HTTPException(status_code=403, detail="Access denied")

    if component_name not in ALLOWED_FIELDS:
        raise HTTPException(status_code=400, detail="Invalid field")

    setattr(category, component_name, new_data)

    await session.commit()
    await session.refresh(category)

    return category

async def delete_category_by_id(session, category_id: int, user_id: int):
    result = await session.execute(delete(CategoryModel).where(CategoryModel.id == category_id, CategoryModel.user_id == user_id))
    await session.commit()

    return result.rowcount
