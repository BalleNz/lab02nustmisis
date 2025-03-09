from models import Order
from controllers import order_controller as calculate_price


def order_info(order: Order):
    print(calculate_price.calculate_order_price(order, 12400))
