import uvicorn
from fastapi import FastAPI

from Python_Final.FastAPI.hw_final.routers import user, product, order
from db import database
from contextlib import asynccontextmanager


# app = FastAPI(lifespan=lifespan)
#
#
# @asynccontextmanager
# async def lifespan(app: FastAPI):
#     await database.connect()
#     yield
#     await database.disconnect()

app = FastAPI()


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


app.include_router(user.router, tags=["users"])
app.include_router(product.router, tags=["products"])
app.include_router(order.router, tags=["orders"])

if __name__ == '__main__':
    uvicorn.run(
        "main:app",
        host="127.0.0.1",
        port=8080,
        reload=True)
