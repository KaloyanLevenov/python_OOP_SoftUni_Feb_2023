from typing import List

from project.computer_types.desktop_computer import DesktopComputer
from project.computer_types.laptop import Laptop


class ComputerStoreApp:

    def __init__(self):
        self.warehouse: List[Laptop, DesktopComputer] = []
        self.profits: int = 0

    def build_computer(self, type_computer: str, manufacturer: str, model: str, processor: str, ram: int):
        if type_computer == 'Desktop Computer':
            computer = DesktopComputer(manufacturer, model)
        elif type_computer == 'Laptop':
            computer = Laptop(manufacturer, model)
        else:
            raise ValueError(f"{type_computer} is not a valid type computer!")

        configuration = computer.configure_computer(processor, ram)
        self.warehouse.append(computer)
        return configuration

    def sell_computer(self, client_budget: int, wanted_processor: str, wanted_ram: int):
        meet_customer_requirements = lambda x: x.price <= client_budget \
                                               and x.processor == wanted_processor \
                                               and x.ram >= wanted_ram
        try:
            computer = (next(filter(meet_customer_requirements, self.warehouse)))
        except StopIteration:
            raise Exception("Sorry, we don't have a computer for you.")

        self.profits += client_budget - computer.price
        self.warehouse.remove(computer)
        return f"{str(computer)} sold for {client_budget}$."


computer_store = ComputerStoreApp()
print(computer_store.build_computer("Laptop", "Apple", "Macbook", "Apple M1 Pro", 64))
print(computer_store.sell_computer(10000, "Apple M1 Pro", 32))
