from models.Order import Order
from views import order_view

if __name__ == "__main__":
    order1 = Order("капот", "серый металлик")
    order_view.order_info(order1)
