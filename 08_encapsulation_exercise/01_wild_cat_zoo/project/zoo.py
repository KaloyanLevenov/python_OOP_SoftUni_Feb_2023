from functools import reduce
from typing import List

from project.caretaker import Caretaker
from project.cheetah import Cheetah
from project.lion import Lion
from project.tiger import Tiger
from project.vet import Vet
from project.worker import Worker


class Zoo:
    def __init__(self, name: str, budget: int, animal_capacity: int, workers_capacity: int):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals: List[object] = []
        self.workers: List[object] = []

    def __have_animal_capacity(self):
        return len(self.animals) < self.__animal_capacity

    def __have_budget(self, price) -> bool:
        return price <= self.__budget

    def __have_worker_capacity(self) -> bool:
        return len(self.workers) < self.__workers_capacity

    def __find_worker(self, name) -> object or None:
        try:
            worker = next(filter(lambda x: x.name == name, self.workers))
            return worker
        except StopIteration:
            return None

    def add_animal(self, animal: object, price: int) -> str:
        if self.__have_animal_capacity() and self.__have_budget(price):
            self.animals.append(animal)
            self.__budget -= price
            return f"{animal.name} the {animal.__class__.__name__} added to the zoo"
        elif self.__have_animal_capacity() and not self.__have_budget(price):
            return "Not enough budget"
        else:
            return "Not enough space for animal"

    def hire_worker(self, worker: object) -> str:
        if self.__have_worker_capacity():
            self.workers.append(worker)
            return f"{worker.name} the {worker.__class__.__name__} hired successfully"
        else:
            return f"Not enough space for worker"

    def fire_worker(self, worker_name) -> str:
        worker = self.__find_worker(worker_name)
        if worker is None:
            return f"There is no {worker_name} in the zoo"
        self.workers.remove(worker)
        return f"{worker_name} fired successfully"

    def pay_workers(self) -> str:

        workers_salary = reduce(lambda a, b: a + b.salary, self.workers, 0)
        if workers_salary <= self.__budget:
            self.__budget -= workers_salary
            return f"You payed your workers. They are happy. Budget left: {self.__budget}"
        return "You have no budget to pay your workers. They are unhappy"

    def tend_animals(self) -> str:
        money_for_the_animals = sum([animal.money_for_care for animal in self.animals])
        if money_for_the_animals <= self.__budget:
            self.__budget -= money_for_the_animals
            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"
        return "You have no budget to tend the animals. They are unhappy."

    def profit(self, amount) -> None:
        self.__budget += amount

    def __counter(self, class_name, lst) -> int:
        counter = 0
        for obj in lst:
            if obj.__class__.__name__ == class_name:
                counter += 1
        return counter

    def animals_status(self) -> str:
        lions = '\n'.join([animal.__repr__() for animal in self.animals if animal.__class__.__name__ == 'Lion'])
        tigers = '\n'.join([animal.__repr__() for animal in self.animals if animal.__class__.__name__ == 'Tiger'])
        cheetahs = '\n'.join([animal.__repr__() for animal in self.animals if animal.__class__.__name__ == 'Cheetah'])

        return f"You have {len(self.animals)} animals\n----- {self.__counter('Lion', self.animals)} Lions:\n{lions}\n" \
               f"----- {self.__counter('Tiger', self.animals)} Tigers:\n{tigers}\n" \
               f"----- {self.__counter('Cheetah', self.animals)} Cheetahs:\n{cheetahs}"

    def workers_status(self) -> str:
        keepers = '\n'.join([worker.__repr__() for worker in self.workers if worker.__class__.__name__ == 'Keeper'])
        caretaker = '\n'.join([worker.__repr__() for worker in self.workers if worker.__class__.__name__ == 'Caretaker'])
        vets = '\n'.join([worker.__repr__() for worker in self.workers if worker.__class__.__name__ == 'Vet'])

        return f"You have {len(self.workers)} workers\n----- {self.__counter('Keeper', self.workers)} Keepers:\n" \
               f"{keepers}\n----- {self.__counter('Caretaker', self.workers)} Caretakers:\n" \
               f"{caretaker}\n----- {self.__counter('Vet', self.workers)} Vets:\n{vets}"
