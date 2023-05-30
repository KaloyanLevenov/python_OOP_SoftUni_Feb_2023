class Account:
    def __init__(self, id_number: int, balance: int, pin: int):
        self.__id = id_number
        self.__pin = pin
        self.balance = balance

    def get_id(self, pin) ->[str or None]:
        if pin == self.__pin:
            return self.__id
        return "Wrong pin"

    def change_pin(self, old_pin, new_pin) -> str:
        if old_pin == self.__pin:
            self.__pin = new_pin
            return "Pin changed"
        return 'Wrong pin'