from fastapi import APIRouter
from app.schemas.order import OrderCreate
from app.services.order_service import create_order, update_order

router = APIRouter(prefix="/orders", tags=["Orders"])

@router.post("/")
def create(order: OrderCreate):
    return create_order(order)

@router.put("/{order_id}")
def update(order_id: int, order: OrderCreate):
    return update_order(order_id, order)
