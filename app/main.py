from fastapi import FastAPI

from app.database.connection import Base

from app.database.connection import (
    engine
)

from app.models import *

from app.routers.auth_router import router as auth

from app.routers.product_router import router as product

from app.routers.supplier_router import router as supplier

from app.routers.stock_router import router as stock


Base.metadata.create_all(
    bind=engine
)


app=FastAPI(

    title="Warehouse Inventory"
)


app.include_router(
    auth
)

app.include_router(
    product
)

app.include_router(
    supplier
)

app.include_router(
    stock
)