from datetime import datetime

class Order:
    def __init__(self, id: int, item: str, price: float):
        self.id = id
        self.item = item
        self.price = price
        self.created_at = datetime.utcnow()
