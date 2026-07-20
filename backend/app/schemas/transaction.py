from datetime import datetime
from pydantic import BaseModel


class TransactionAddSchema(BaseModel):
    name: str
    description: str | None = None
    amount: float
    type: str
    currency: str = "UAH"
    account_name: str | None = None
    category_id: int
    user_id: int

class TransactionSchema(TransactionAddSchema):
    id: int

    class Config:
        from_attributes = True
