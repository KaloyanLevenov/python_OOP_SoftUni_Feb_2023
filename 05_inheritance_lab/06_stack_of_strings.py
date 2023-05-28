from typing import List


class Stack:
    def __init__(self):
        self.data: List = []

    def push(self, element) -> None:
        self.data.append(element) if isinstance(element, str) else None

    def pop(self):
        return self.data.pop()

    def top(self):
        return self.data[-1]

    def is_empty(self):
        return len(self.data) == 0

    def __str__(self):  # [{element(N)}, {element(N-1)} ... {element(0)}]
        return "[" + ', '.join([self.data[x] for x in range(len(self.data) - 1, -1, -1)]) + "]"
