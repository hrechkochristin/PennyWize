from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from backend.app.models.base import Base
from backend.app.routers import transaction, user, category
from backend.app.core.database import engine

app = FastAPI()

# Дозволяємо React звертатися до API
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(transaction.router)
app.include_router(user.router)
app.include_router(category.router)


@app.get("/")
async def root():
    return {"message": "API is running"}