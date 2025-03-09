def load_base():
    with open("data/order_price_course_colors", "r") as colors_price:
        dict_colors = {" ".join(line.split()[:-1]).lower(): float(line.split()[-1]) for line in colors_price}

    with open("data/order_price_course_details", "r") as details_price:
        dict_details = {" ".join(line.split()[:-1]).lower(): float(line.split()[-1]) for line in details_price}

    return dict_colors, dict_details
