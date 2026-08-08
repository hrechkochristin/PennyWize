from datetime import datetime

from fastapi import HTTPException
from sqlalchemy import select, delete, desc, asc
from sqlalchemy.orm import selectinload

from backend.app.core.database import offset, limit
from backend.app.core.range import RangeField, RangeFieldType, RANGE_FIELDS
from backend.app.core.sort import SORT_FIELDS, SortOrder
from backend.app.models.transaction import TransactionModel
from backend.app.schemas.transaction import TransactionAddSchema


async def create_transaction(session, data: TransactionAddSchema, user_id: int):
    new_transaction = TransactionModel(
        name=data.name,
        description=data.description,
        amount=data.amount,
        type=data.type,
        currency=data.currency,
        account_name=data.account_name,
        category_id=data.category_id,
        user_id=user_id,
    )
    session.add(new_transaction)
    await session.commit()
    await session.refresh(new_transaction)
    return new_transaction


def convert_value(value, range_by):
    if value is None:
        return None

    if range_by == RangeField.date:
        return datetime.fromisoformat(value)

    return RangeFieldType[range_by.value](value)

async def read_transactions(session, user_id: int, sort_by, order, range_by, min_value, max_value, type=None, currency=None, category_id=None):
    query = (select(TransactionModel)
        .options(selectinload(TransactionModel.category))
        .where(TransactionModel.user_id == user_id))

    if type is not None:
        query = query.where(TransactionModel.type == type)
    if currency is not None:
        query = query.where(TransactionModel.currency == currency)
    if category_id is not None:
        query = query.where(TransactionModel.category_id == category_id)

    sort_column = SORT_FIELDS[sort_by]

    if order == SortOrder.asc:
        query = query.order_by(asc(sort_column))
    else:
        query = query.order_by(desc(sort_column))

    range_column = RANGE_FIELDS[range_by]

    min_value = convert_value(min_value, range_by)
    max_value = convert_value(max_value, range_by)

    if min_value is not None:
        query = query.where(range_column >= min_value)

    if max_value is not None:
        query = query.where(range_column <= max_value)

    result = await session.execute(query.limit(limit).offset(offset))

    return result.scalars().all()

async def delete_transactions(session, user_id: int, type=None, currency=None, category_id=None):
    query = delete(TransactionModel).where(TransactionModel.user_id == user_id)

    if type is not None:
        query = query.where(TransactionModel.type == type)
    if currency is not None:
        query = query.where(TransactionModel.currency == currency)
    if category_id is not None:
        query = query.where(TransactionModel.category_id == category_id)

    result = await session.execute(query)
    await session.commit()

    return bool(result.rowcount)

async def read_transaction_by_id(session, transaction_id: int, user_id: int):
    result = await session.execute(select(TransactionModel).where(TransactionModel.id == transaction_id))
    transaction = result.scalars().one_or_none()

    if not transaction:
        return None

    if transaction.user_id != user_id:
        raise HTTPException(status_code=403, detail="Access denied")

    return transaction

ALLOWED_FIELDS = {
    "name",
    "description",
    "amount",
    "type",
    "currency",
    "account_name",
    "date",
    "category_id",
}

async def update_transaction_by_id(session, transaction_id: int, user_id: int, component_name: str, new_data: str):
    result = await session.execute(select(TransactionModel).where(TransactionModel.id == transaction_id))
    transaction = result.scalars().one_or_none()

    if not transaction:
        return None

    if transaction.user_id != user_id:
        raise HTTPException(status_code=403, detail="Access denied")

    if component_name not in ALLOWED_FIELDS:
        raise HTTPException(status_code=400, detail="Invalid field")

    setattr(transaction, component_name, new_data)

    await session.commit()
    await session.refresh(transaction)

    return transaction

async def delete_transaction_by_id(session, transaction_id: int, user_id: int):
    result = await session.execute(delete(TransactionModel).where(TransactionModel.id == transaction_id, TransactionModel.user_id == user_id))
    await session.commit()

    return result.rowcount