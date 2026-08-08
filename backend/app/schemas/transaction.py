from datetime import datetime
from pydantic import BaseModel, ConfigDict

from backend.app.schemas.category import CategoryResponseSchema


class TransactionAddSchema(BaseModel):
    name: str
    description: str | None = None
    amount: float
    type: str
    currency: str = "UAH"
    account_name: str | None = None
    category_id: int

class TransactionSchema(TransactionAddSchema):
    id: int
    date: datetime

    class Config:
        from_attributes = True


class TransactionResponseSchema(BaseModel):
    id: int
    name: str
    description: str | None
    amount: float
    type: str
    currency: str
    account_name: str | None
    date: datetime

    category: CategoryResponseSchema

    model_config = ConfigDict(from_attributes=True)