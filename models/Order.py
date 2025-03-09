class Order:
    def __init__(self, detail: str, color: str):
        self.__detail = detail
        self.__color = color

    @property
    def color(self):
        return self.__color

    @property
    def detail(self):
        return self.__detail
