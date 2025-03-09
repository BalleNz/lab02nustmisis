def get_dict_details():
    with open("data/order_price_course_details", "r") as details_price:
        return {" ".join(line.split()[:-1]).lower(): float(line.split()[-1]) for line in details_price}


def get_dict_colors():
    with open("data/order_price_course_colors", "r") as colors_price:
        return {" ".join(line.split()[:-1]).lower(): float(line.split()[-1]) for line in colors_price}
