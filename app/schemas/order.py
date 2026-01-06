from pydantic import BaseModel

class OrderCreate(BaseModel):
    item: str
    price: float

class OrderResponse(BaseModel):
    id: int
    item: str
    price: float
    gst_amount: float
    total_amount: float
