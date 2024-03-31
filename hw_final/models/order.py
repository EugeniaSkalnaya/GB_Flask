from datetime import datetime
from pydantic import BaseModel, Field


class OrderCreate(BaseModel):
    user_id: int
    prod_id: int
    date: datetime = Field(default=datetime.now())
    status: str = Field(default="created")


class OrderRead(BaseModel):
    id: int
    user_id: int
    prod_id: int
    date: str
    status: str = Field(default="created")
