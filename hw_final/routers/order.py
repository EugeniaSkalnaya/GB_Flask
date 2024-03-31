import datetime
from random import randint
from typing import List
from fastapi import APIRouter, HTTPException
from Python_Final.FastAPI.hw_final import db
from Python_Final.FastAPI.hw_final.db import orders, database
from Python_Final.FastAPI.hw_final.models.order import OrderRead, OrderCreate

router = APIRouter()


@router.get("/fake_orders/{count}")
async def create_fake_orders(count: int):
    for i in range(count):
        query = db.orders.insert().values(
            user_id=randint(1, 20),
            prod_id=randint(1, 20),
            status="created",
            date=datetime.datetime.now())
        await db.database.execute(query)
    return {'message': f'{count} fake orders create'}


@router.post("/order", response_model=OrderCreate)
async def create_order(order: OrderCreate):
    query = orders.insert().values(
        user_id=order.user_id,
        prod_id=order.prod_id,
        status=order.status,
        date=datetime.datetime.now()
    )
    await database.execute(query)
    return order


@router.get("/orders/", response_model=List[OrderRead])
async def read_orders():
    query = db.orders.select()
    return await db.database.fetch_all(query)


@router.get("/orders/{order_id}", response_model=OrderRead)
async def read_order(order_id: int):
    query = db.orders.select().where(db.orders.c.id == order_id)
    order = await db.database.fetch_one(query)
    if order is None:
        raise HTTPException(status_code=404, detail="Order not found")
    return order


@router.put("/orders/{order_id}", response_model=OrderRead)
async def update_order(order_id: int, new_order: OrderCreate):
    query = db.orders.update().where(db.orders.c.id == order_id).values(**new_order.dict())
    await db.database.execute(query)
    return {**new_order.dict(), "id": order_id}


@router.delete("/orders/{order_id}")
async def delete_order(order_id: int):
    query = db.orders.delete().where(db.orders.c.id == order_id)
    await db.database.execute(query)
    return {'message': 'Order deleted'}