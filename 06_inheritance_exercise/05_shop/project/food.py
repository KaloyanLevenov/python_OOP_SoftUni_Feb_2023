from project.product import Product


class Food(Product):
    QUANTITY = 15

    def __init__(self, name: str, quantity: int = QUANTITY):
        super().__init__(name, quantity)

