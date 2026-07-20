from fastapi import APIRouter

from backend.app.crud.transaction import create_transaction, read_transactions, read_transaction_by_id, \
    update_transaction_by_id, delete_transaction_by_id, delete_transactions
from backend.app.schemas.transaction import TransactionSchema, TransactionAddSchema
from backend.app.core.database import SessionDep

router = APIRouter(prefix="/transactions", tags=["Transactions"])


@router.post("/create/{user_id}", response_model=TransactionSchema)
async def add_transaction(data: TransactionAddSchema, session: SessionDep, user_id: int):
    return await create_transaction(session, data, user_id)


@router.get("/read_all/{user_id}", response_model=list[TransactionSchema])
async def get_transactions(session: SessionDep, user_id: int):
    return await read_transactions(session, user_id)

@router.get("/read_by_id/{user_id}", response_model=TransactionSchema)
async def get_transaction_by_id(session: SessionDep, transaction_id: int, user_id: int):
    return await read_transaction_by_id(session, transaction_id, user_id)

@router.patch("/update_by_id/{user_id}", response_model=TransactionSchema)
async def renew_transaction_by_id(session: SessionDep, transaction_id: int, user_id: int, component_name: str, new_data: str):
    return await update_transaction_by_id(session, transaction_id, user_id, component_name, new_data)

@router.post("/delete_by_id/{user_id}", response_model=bool)
async def remove_transaction_by_id(session: SessionDep, transaction_id: int, user_id: int):
    return await delete_transaction_by_id(session, transaction_id, user_id)

@router.post("/delete_all/{user_id}", response_model=bool)
async def remove_transactions(session: SessionDep, user_id: int):
    return await delete_transactions(session, user_id)