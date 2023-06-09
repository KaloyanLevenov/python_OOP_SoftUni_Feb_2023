class custom_range:
    def __init__(self, start: int, end: int):
        self.start = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.start <= self.end:
            number = self.start
            self.start += 1
            return number
        else:
            raise StopIteration


test = custom_range(1, 10)
for element in test:
    print(element, end=" ")
