from project.beverage.hot_beverage import HotBeverage


class Coffee(HotBeverage):
    MILLILITERS = 50
    PRICE = 3.50

    def __init__(self, name: str, caffeine: float, milliliters: float = MILLILITERS, price: float = PRICE):
        super().__init__(name, price, milliliters)
        self.__caffeine = caffeine

    @property
    def caffeine(self):
        return self.__caffeine

coffee = Coffee('ARABICA', 50, 10, 50)
print(coffee.name)