class Vehicle:
    DEFAULT_FUEL_CONSUMPTION: float = 1.25

    def __init__(self, fuel: float, horse_power: int):
        self.fuel_consumption: float = self.DEFAULT_FUEL_CONSUMPTION
        self.fuel = fuel
        self.horse_power = horse_power

    def drive(self, kilometers):
        fuel_to_reduce = kilometers * self.fuel_consumption
        self.fuel -= fuel_to_reduce if fuel_to_reduce <= self.fuel else 0