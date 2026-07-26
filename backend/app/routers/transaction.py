from fastapi import APIRouter, Depends

from backend.app.crud.transaction import create_transaction, read_transactions, read_transaction_by_id, \
    update_transaction_by_id, delete_transaction_by_id, delete_transactions
from backend.app.crud.user import get_current_user
from backend.app.models import UserModel
from backend.app.schemas.transaction import TransactionSchema, TransactionAddSchema
from backend.app.core.database import SessionDep

router = APIRouter(prefix="/transactions", tags=["Transactions"])

# Creating custom user's transaction
@router.post("", response_model=TransactionSchema)
async def add_transaction(data: TransactionAddSchema, session: SessionDep, current_user: UserModel = Depends(get_current_user)):
    return await create_transaction(session, data, current_user.id)

# Reading all user's custom transactions
@router.get("", response_model=list[TransactionSchema])
async def get_transactions(session: SessionDep, current_user: UserModel = Depends(get_current_user)):
    return await read_transactions(session, current_user.id)

# Deleting all user's custom transactions
@router.delete("", response_model=bool)
async def remove_transactions(session: SessionDep, current_user: UserModel = Depends(get_current_user)):
    return await delete_transactions(session, current_user.id)

# Reading user's transaction by id (if transaction doesn't belong to user it's invisible)
@router.get("/{transaction_id}", response_model=TransactionSchema)
async def get_transaction_by_id(session: SessionDep, transaction_id: int, current_user: UserModel = Depends(get_current_user)):
    return await read_transaction_by_id(session, transaction_id, current_user.id)

# Updating user's transaction attributes by id (if transaction doesn't belong to user it's invisible)
@router.patch("/{transaction_id}", response_model=TransactionSchema)
async def renew_transaction_by_id(session: SessionDep, transaction_id: int, component_name: str, new_data: str, current_user: UserModel = Depends(get_current_user)):
    return await update_transaction_by_id(session, transaction_id, current_user.id, component_name, new_data)

# Deleting user's transaction by id (if transaction doesn't belong to user it's invisible)
@router.delete("/{transaction_id}", response_model=bool)
async def remove_transaction_by_id(session: SessionDep, transaction_id: int, current_user: UserModel = Depends(get_current_user)):
    return await delete_transaction_by_id(session, transaction_id, current_user.id)