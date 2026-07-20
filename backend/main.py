from fastapi import FastAPI

from backend.app.models.base import Base
from backend.app.routers import transaction, user, category
from backend.app.core.database import engine

app = FastAPI()

app.include_router(transaction.router)
app.include_router(user.router)
app.include_router(category.router)

@app.get("/")
async def root():
    return {"message": "API is running"}

transactions = [
    {
        "id": "tx_001",
        "name": "Сільпо",
        "description": "Продукти на тиждень та смаколики",
        "category": "Продукти",
        "amount": 450.50,
        "type": "expense",
        "currency": "UAH",
        "card_number": "4441 •••• •••• 1234",
        "date": "2026-07-15T18:30:00Z"
    },
    {
        "id": "tx_002",
        "name": "Аванс",
        "description": "Часткова виплата заробітної плати",
        "category": "Робота",
        "amount": 12000.00,
        "type": "income",
        "currency": "UAH",
        "card_number": "4441 •••• •••• 1234",
        "date": "2026-07-16T10:15:00Z"
    },
    {
        "id": "tx_003",
        "name": "Кав'ярня 'Альтернатива'",
        "description": "Капучино та круасан",
        "category": "Кафе та ресторани",
        "amount": 145.00,
        "type": "expense",
        "currency": "UAH",
        "card_number": "5375 •••• •••• 5678",
        "date": "2026-07-17T09:45:00Z"
    },
    {
        "id": "tx_004",
        "name": "Підписка Spotify",
        "description": "Місячна підписка Premium",
        "category": "Розваги",
        "amount": 4.99,
        "type": "expense",
        "currency": "USD",
        "card_number": "5375 •••• •••• 5678",
        "date": "2026-07-18T00:00:00Z"
    }
]

# @app.get("/dashboard")
# def read_dashboard():
#     return {"transactions": transactions }
