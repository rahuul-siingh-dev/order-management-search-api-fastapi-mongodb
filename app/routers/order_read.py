from fastapi import APIRouter
from app.services.order_service import list_orders, get_order_by_id

router = APIRouter(prefix="/orders", tags=["Orders"])

@router.get("/")
def get_orders():
    return list_orders()

@router.get("/{order_id}")
def get_order(order_id: int):
    return get_order_by_id(order_id)
