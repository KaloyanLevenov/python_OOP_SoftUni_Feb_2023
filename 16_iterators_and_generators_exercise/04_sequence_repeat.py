class sequence_repeat:
    """Create a class called sequence_repeat which should receive a sequence and a number upon initialization.
    Implement an iterator to return the given elements, so they form a string with a length - the given number.
    If the number is greater than the number of elements, then the sequence repeats as necessary.
    For more clarification, see the examples:"""

    def __init__(self, sequence, number: int):
        self.sequence = sequence
        self.number = number
        self.repetition = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.repetition < self.number:
            index = self.repetition % len(self.sequence)
            self.repetition += 1
            result = self.sequence[index]
            return result
        else:
            raise StopIteration


result = sequence_repeat('abc', 5)
for item in result:
    print(item, end ='')