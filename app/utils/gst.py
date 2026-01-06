def calculate_gst(price: float):
    gst_amount = price * 0.18
    total_amount = price + gst_amount
    return round(gst_amount, 2), round(total_amount, 2)

