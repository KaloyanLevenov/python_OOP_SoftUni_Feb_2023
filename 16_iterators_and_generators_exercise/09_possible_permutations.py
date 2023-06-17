import itertools
from typing import List
from itertools import permutations


def possible_permutations(lst: List[int]):
    result = list(permutations(lst))
    for permutation in result:
        yield list(permutation)

[print(n) for n in possible_permutations([1, 2, 3])]
