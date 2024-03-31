from random import randint
from typing import List
from fastapi import APIRouter, HTTPException
from Python_Final.FastAPI.hw_final import db
from Python_Final.FastAPI.hw_final.db import products, database
from Python_Final.FastAPI.hw_final.models.product import ProductRead, ProductCreate

router = APIRouter()


@router.get("/fake_products/{count}")
async def create_fake_products(count: int):
    for i in range(count):
        query = db.products.insert().values(
            title=f'product {i}',
            description=f'Usefull info about product {i}',
            price=randint(1, 5000))
        await db.database.execute(query)
    return {'message': f'{count} fake products create'}


@router.post("/product", response_model=ProductCreate)
async def create_product(product: ProductCreate):
    query = products.insert().values(
        title=product.title,
        description=product.lastname,
        price=product.price,
    )
    await database.execute(query)
    return product


@router.get('/products/', response_model=List[ProductRead])
async def read_all_products():
    return await database.fetch_all(products.select())


@router.get("/products/{product_id}", response_model=ProductRead)
async def read_product(product_id: int):
    query = db.products.select().where(db.products.c.id == product_id)
    product = await db.database.fetch_one(query)
    if product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return product


@router.put("/products/{product_id}", response_model=ProductRead)
async def update_product(product_id: int, new_product: ProductCreate):
    query = db.products.update().where(db.products.c.id == product_id).values(**new_product.dict())
    await db.database.execute(query)
    return {**new_product.dict(), "id": product_id}


@router.delete("/products/{product_id}")
async def delete_product(product_id: int):
    query = db.products.delete().where(db.products.c.id == product_id)
    await db.database.execute(query)
    return {'message': 'Product deleted'}