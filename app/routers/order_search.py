from fastapi import APIRouter
from app.services.order_service import search_orders

router = APIRouter(prefix="/orders/search", tags=["Order Search"])

@router.get("/")
def search(query: str = "", min_price: float = 0):
    return search_orders(query, min_price)
