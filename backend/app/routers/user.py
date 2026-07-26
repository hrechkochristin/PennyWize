from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

from backend.app.crud.user import login_user, signup_user, get_current_user
from backend.app.models import UserModel
from backend.app.schemas.user import UserSignUpSchema
from backend.app.core.database import SessionDep, get_session

router = APIRouter(prefix="/users", tags=["Users"])

@router.post("/signup")
async def signup(user_data: UserSignUpSchema, session=Depends(get_session)):
    return await signup_user(user_data, session)

@router.post("/login")
async def login(form_data: OAuth2PasswordRequestForm = Depends(), session=Depends(get_session)):
    return await login_user(form_data, session)

@router.get("/me")
async def get_me(current_user: UserModel = Depends(get_current_user)):
    return {
        "id": current_user.id,
        "username": current_user.username,
        "email": current_user.email
    }