class countdown_iterator:
    """Create a class called countdown_iterator. Upon initialization, it should receive a count.
    Implement the iterator to return each countdown number (from count to 0 inclusive), separated by a single space."""
    def __init__(self, count: int):
        self.count = count

    def __iter__(self):
        return self

    def __next__(self):
        if self.count >= 0:
            number = self.count
            self.count -= 1
            return number
        else:
            raise StopIteration


iterator = countdown_iterator(0)
for item in iterator:
    print(item, end=" ")