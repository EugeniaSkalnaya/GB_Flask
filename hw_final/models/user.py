from pydantic import BaseModel, Field


class UserCreate(BaseModel):
    firstname: str = Field(max_length=32)
    lastname: str = Field(max_length=32)
    email: str = Field(max_length=128)
    password: str = Field(min_length=3)


class UserRead(BaseModel):
    id: int
    firstname: str = Field(max_length=32)
    lastname: str = Field(max_length=32)
    email: str = Field(max_length=128)

