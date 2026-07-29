import enum
from datetime import datetime

from backend.app.models import TransactionModel


class RangeField(str, enum.Enum):
    id = "id"
    user_id = "user_id"
    amount = "amount"
    date = "date"

RangeFieldType = {
    "id" : int,
    "user_id" : int,
    "amount" : float,
    "date" : datetime
}

RANGE_FIELDS = {
    RangeField.id: TransactionModel.id,
    RangeField.user_id: TransactionModel.user_id,
    RangeField.amount: TransactionModel.amount,
    RangeField.date: TransactionModel.date,
}