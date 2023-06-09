class Robot:
    SENSORS_AMOUNT = 1

    def __init__(self, name):
        self.name = name

    @classmethod
    def sensors_amount(cls):
        return cls.SENSORS_AMOUNT


class MedicalRobot(Robot):
    SENSORS_AMOUNT = 6


class ChefRobot(Robot):
    SENSORS_AMOUNT = 4


class WarRobot(Robot):
    SENSORS_AMOUNT = 12


basic_robot = Robot('Robo')
da_vinci = MedicalRobot('Da Vinci')
moley = ChefRobot('Moley')
griffin = WarRobot('Griffin')
print(WarRobot.sensors_amount())