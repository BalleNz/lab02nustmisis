from controllers import database_controller
from models import Order


def calculate_order_price(order: Order, price: int) -> int:
    dict_colors, dict_details = database_controller.load_base()
    return price * dict_colors[order.color] + price * dict_details[order.detail]
