from fastapi import FastAPI
from app.routers import order_read, order_write, order_search

app = FastAPI(title="Order Management & Search API")

app.include_router(order_read.router)
app.include_router(order_write.router)
app.include_router(order_search.router)
