from pydantic import BaseModel, Field


class ProductCreate(BaseModel):
    title: str = Field(max_length=50)
    description: str = Field(max_length=300)
    price: float = Field(default=0)


class ProductRead(BaseModel):
    id: int
    title: str = Field(max_length=50)
    description: str = Field(max_length=300)
    price: float = Field(default=0)
