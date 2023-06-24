from math import log2
from abc import ABC, abstractmethod


class Computer(ABC):
    def __init__(self, manufacturer: str, model: str):
        self.manufacturer = manufacturer
        self.model = model
        self.processor: str = None
        self.ram: int = None
        self.price: int = 0

    @property
    def manufacturer(self):
        return self.__manufacturer

    @manufacturer.setter
    def manufacturer(self, value):
        if value.strip() == '':
            raise ValueError("Manufacturer name cannot be empty.")

        self.__manufacturer = value

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, value):
        if value.strip() == '':
            raise ValueError("Model name cannot be empty.")

        self.__model = value

    @property
    def valid_types(self):
        return "Laptop", "Desktop Computer"

    @property
    @abstractmethod
    def available_processors(self):
        pass

    @property
    @abstractmethod
    def max_ram(self):
        pass

    @property
    def ram_price(self):
        multiplier = log2(self.ram)
        price = 100 * multiplier
        return price

    @property
    @abstractmethod
    def type_computer(self):
        ...

    def configure_computer(self, processor: str, ram: int):
        if processor not in self.available_processors.keys():
            raise ValueError(f"{processor} is not compatible with {self.type_computer} {self.manufacturer} {self.model}!")
        else:
            processor_is_valid = True

        if not isinstance(ram, int) or log2(ram) not in range(int(log2(self.max_ram) + 1)):
            raise ValueError(f"{ ram }GB RAM is not compatible with "
                             f"{self.type_computer} { self.manufacturer } { self.model }!")
        else:
            ram_is_valid = True

        if processor_is_valid and ram_is_valid:
            self.processor = processor
            self.ram = ram
            self.price = self.ram_price + self.available_processors[processor]
            return f"Created {self.manufacturer} {self.model} " \
                   f"with {processor} and {ram}GB RAM for {self.price:.0f}$."

    def __repr__(self):
        return f"{self.__manufacturer} {self.__model} with {self.processor} and {self.ram}GB RAM"
