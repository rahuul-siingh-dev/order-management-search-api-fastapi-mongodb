from app.models.order import Order
from app.utils.gst import calculate_gst

# In-memory DB (replace with MongoDB later)
ORDERS_DB = [
    Order(101, "Laptop", 1000),
    Order(102, "Mobile", 500)
]

def list_orders():
    result = []
    for order in ORDERS_DB:
        gst, total = calculate_gst(order.price)
        result.append({
            "id": order.id,
            "item": order.item,
            "price": order.price,
            "gst_amount": gst,
            "total_amount": total
        })
    return result

def get_order_by_id(order_id: int):
    for order in ORDERS_DB:
        if order.id == order_id:
            gst, total = calculate_gst(order.price)
            return {
                "id": order.id,
                "item": order.item,
                "price": order.price,
                "gst_amount": gst,
                "total_amount": total
            }
    return {"error": "Order not found"}

def create_order(order_data):
    new_id = max(o.id for o in ORDERS_DB) + 1
    order = Order(new_id, order_data.item, order_data.price)
    ORDERS_DB.append(order)
    return {"message": "Order created", "order_id": new_id}

def update_order(order_id: int, order_data):
    for order in ORDERS_DB:
        if order.id == order_id:
            order.item = order_data.item
            order.price = order_data.price
            return {"message": "Order updated"}
    return {"error": "Order not found"}

def search_orders(query: str, min_price: float):
    results = []
    for order in ORDERS_DB:
        if query.lower() in order.item.lower() and order.price >= min_price:
            gst, total = calculate_gst(order.price)
            results.append({
                "id": order.id,
                "item": order.item,
                "price": order.price,
                "gst_amount": gst,
                "total_amount": total
            })
    return results
