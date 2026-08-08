from pydantic import BaseModel, ConfigDict


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

class CategoryResponseSchema(BaseModel):
    id: int
    name: str
    description: str | None
    icon: str | None
    color: str

    model_config = ConfigDict(from_attributes=True)