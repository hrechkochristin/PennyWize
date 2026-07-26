from fastapi import HTTPException
from sqlalchemy import select, delete

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


async def read_transactions(session, user_id: int):
    result = await session.execute(select(TransactionModel).where(TransactionModel.user_id == user_id))
    return result.scalars().all()

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

async def delete_transactions(session, user_id: int):
    result = await session.execute(delete(TransactionModel).where(TransactionModel.user_id == user_id))
    await session.commit()

    return bool(result.rowcount)