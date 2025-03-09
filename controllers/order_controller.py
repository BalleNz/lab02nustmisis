from controllers import database_controller
from models import Order


def calculate_order_price(order: Order, price: int) -> int:
    dict_colors, dict_details = database_controller.get_dict_colors(), database_controller.get_dict_details()
    return price * dict_colors[order.color] + price * dict_details[order.detail]
