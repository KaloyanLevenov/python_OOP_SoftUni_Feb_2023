def read_next(*args):
    """Create a generator function called read_next()
    which should receive a different number of arguments (all iterable).
    On each iteration, the function should return each element from each sequence."""
    for element in args:
        for char in element:
            yield char


for item in read_next("string", (2,), {"d": 1, "i": 2, "c": 3, "t": 4}):
    print(item, end='')