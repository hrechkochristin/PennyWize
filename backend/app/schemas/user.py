from pydantic import BaseModel


class UserSignUpSchema(BaseModel):
    username: str
    email: str
    password: str

# class UserLogInSchema(BaseModel):
#     username: str
#     password: str

class UserSchema(BaseModel):
    id: int
    username: str
    email: str

    class Config:
        from_attributes = True
