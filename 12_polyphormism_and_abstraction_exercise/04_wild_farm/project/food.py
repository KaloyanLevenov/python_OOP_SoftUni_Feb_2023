from abc import ABC, abstractmethod


class Food(ABC):
    @abstractmethod
    def __init__(self, quantity: int):
        self.quantity = quantity


# Vegetable, Fruit, Meat and Seed classes should inherit from the Food class

class Vegetable(Food):
    def __init__(self, quantity: int):
        super().__init__(quantity)


class Fruit(Food):
    def __init__(self, quantity: int):
        super().__init__(quantity)


class Meat(Food):
    def __init__(self, quantity: int):
        super().__init__(quantity)


class Seed(Food):
    def __init__(self, quantity: int):
        super().__init__(quantity)

