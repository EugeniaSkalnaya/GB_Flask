from fastapi import APIRouter, HTTPException
from sqlalchemy import select

from Python_Final.FastAPI.hw_final.db import users, database
from Python_Final.FastAPI.hw_final.models.user import UserCreate, UserRead

router = APIRouter()


@router.get("/fake_users/{count}")
async def create_fake(count: int):
    for i in range(count):
        query = users.insert().values(
            firstname=f'firstname{i}',
            lastname=f'lastname{i}',
            email=f'mail{i}@mail.ru',
            password=f'password{i}')
        await database.execute(query)
    return {'message': f'{count} fake users create'}


@router.post("/user", response_model=UserCreate)
async def create_user(user: UserCreate):
    query = users.insert().values(
        firstname=user.firstname,
        lastname=user.lastname,
        email=user.email,
        password=user.password
    )
    await database.execute(query)
    return user


@router.get("/users/", response_model=list[UserRead])
async def read_users():
    query = select(users.c.id, users.c.firstname, users.c.lastname, users.c.email)
    return await database.fetch_all(query)


@router.get("/users/{user_id}", response_model=UserRead)
async def read_user(user_id: int):
    query = users.select().where(users.c.id == user_id)
    if not query:
        raise HTTPException(status_code=404, detail="User not found")
    return await database.fetch_one(query)


@router.put('/users/{user_id}', response_model=UserRead)
async def update_user(user_id: int, new_user: UserCreate):
    query = users.update().where(users.c.id == user_id).values(
        **new_user.model_dump())
    await database.execute(query)
    return {**new_user.model_dump(), 'id': user_id}


@router.delete("/users/{user_id}")
async def delete_user(user_id: int):
    query = users.delete().where(users.c.id == user_id)
    await database.execute(query)
    return {'message': 'User deleted'}
