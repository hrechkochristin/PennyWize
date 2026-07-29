import enum
from backend.app.models.transaction import TransactionModel

class SortField(str, enum.Enum):
    amount = "amount"
    type = "type"
    currency = "currency"
    account_name = "account_name"
    date = "date"


class SortOrder(str, enum.Enum):
    asc = "asc"
    desc = "desc"


SORT_FIELDS = {
    SortField.amount: TransactionModel.amount,
    SortField.type: TransactionModel.type,
    SortField.currency: TransactionModel.currency,
    SortField.account_name: TransactionModel.account_name,
    SortField.date: TransactionModel.date,
}