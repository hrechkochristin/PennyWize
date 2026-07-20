from pydantic import BaseModel

class CategoryAddSchema(BaseModel):
    name: str
    description: str | None = None
    icon: str | None = None
    color: str
    user_id: int | None = None

class CategorySchema(CategoryAddSchema):
    id: int
    
    class Config:
        from_attributes = True
