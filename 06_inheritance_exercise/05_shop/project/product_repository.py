from typing import List

from project.drink import Drink
from project.food import Food
from project.product import Product


class ProductRepository:
    def __init__(self):
        self.products: List[object] = []

    def add(self, product: Product) -> None:
        self.products.append(product)

    def find(self, product_name: str) -> [object, None]:
        try:
            product = next(filter(lambda x: x.name == product_name, self.products))
        except StopIteration:
            return None
        return product

    def remove(self, product_name):
        product = self.find(product_name)
        self.products.remove(product) if product else None

    def __repr__(self):
        return '\n'.join([f"{p.name}: {p.quantity}" for p in self.products])


food = Food("apple")
drink = Drink("water")
repo = ProductRepository()
repo.add(food)
repo.add(drink)
print(repo.products)
print(repo.find("water"))
repo.find("apple").decrease(5)
print(repo)