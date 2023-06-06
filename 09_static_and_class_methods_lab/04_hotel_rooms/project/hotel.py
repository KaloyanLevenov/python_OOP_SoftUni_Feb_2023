from typing import List
from project.room import Room


class Hotel:
    def __init__(self, name: str):
        self.name = name
        self.rooms: List[Room] = []
        self.guests: int = 0

    @classmethod
    def from_stars(cls, stars_count: int):
        return cls(f"{stars_count} stars Hotel")

    def add_room(self, room: Room) -> None:
        self.rooms.append(room)

    def __find_room(self, room_number: int):
        room = next(filter(lambda x: x.number == room_number, self.rooms))
        return room

    def take_room(self, room_number: int, people: int):
        room = self.__find_room(room_number)
        result = room.take_room(people)
        if result is None:  # it does not returns a string with message it can not be taken, so it means it is taken
            self.guests += people
            return
        return result

    def free_room(self, room_number):
        room = self.__find_room(room_number)
        guests = room.guests
        result = room.free_room()
        if result is None:
            self.guests -= guests
        return result

    def status(self) -> str:
        return f"Hotel {self.name} has {self.guests} total guests\n" \
               f"Free rooms: {', '.join(str(room.number) for room in self.rooms if room.is_taken == False)}\n" \
               f"Taken rooms: {', '.join(str(room.number) for room in self.rooms if room.is_taken == True)}"
