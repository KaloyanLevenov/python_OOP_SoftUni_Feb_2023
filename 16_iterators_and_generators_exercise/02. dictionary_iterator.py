class dictionary_iter:
    def __init__(self, dictionary: dict):
        self.dictionary = dictionary
        self.items = list(self.dictionary.items())

    def __iter__(self):
        return self

    def __next__(self):
        while self.items:
            return self.items.pop(0)
        else:
            raise StopIteration


result = dictionary_iter({1: "1", 2: "2"})
for x in result:
    print(x)

