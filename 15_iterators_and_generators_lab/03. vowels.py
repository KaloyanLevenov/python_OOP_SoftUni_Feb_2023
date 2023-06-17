class vowels:
    VOWELS = ['a', 'e', 'i', 'o', 'u', 'y']

    def __init__(self, string):
        self.string = string
        self.result = [char for char in self.string if char.lower() in self.VOWELS]

    def __iter__(self):
        return self

    def __next__(self):

        while self.result:
            return self.result.pop(0)
        else:
            raise StopIteration





my_string = vowels('Abcedifuty0o')
for char in my_string:
    print(char)