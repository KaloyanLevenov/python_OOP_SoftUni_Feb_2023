from abc import ABC, abstractmethod


class Vehicle(ABC):

    def __init__(self, fuel_quantity: int, fuel_consumption: int):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    @abstractmethod
    def drive(self, distance):
        pass

    @abstractmethod
    def refuel(self, fuel):
        pass


class Car(Vehicle):
    FUEL_CONSUMPTION_ADDITION = 0.9

    def __init__(self, fuel_quantity: int, fuel_consumption: int):
        super().__init__(fuel_quantity, fuel_consumption)

    def drive(self, distance):
        fuel_needed = distance * (self.fuel_consumption + self.FUEL_CONSUMPTION_ADDITION)
        if self.fuel_quantity >= fuel_needed:
            self.fuel_quantity -= fuel_needed

    def refuel(self, fuel):
        self.fuel_quantity += fuel


class Truck(Vehicle):
    FUEL_CONSUMPTION_ADDITION = 1.60

    def __init__(self, fuel_quantity: int, fuel_consumption: int):
        super().__init__(fuel_quantity, fuel_consumption)

    def drive(self, distance):
        fuel_needed = distance * (self.fuel_consumption + self.FUEL_CONSUMPTION_ADDITION)
        if self.fuel_quantity >= fuel_needed:
            self.fuel_quantity -= fuel_needed

    def refuel(self, fuel):
        self.fuel_quantity += fuel * 0.95