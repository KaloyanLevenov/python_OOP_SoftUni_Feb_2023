from typing import List


def get_primes(iterable: List[int]):
    for number in iterable:
        if number <= 1:
            continue

        for i in range(2, int(number / 2) + 1):
            # If number is divisible by any number between
            # 2 and number / 2, it is not prime
            if (number % i) == 0:
                break
        else:
            yield number



print(list(get_primes([2, 4, 3, 5, 6, 9, 1, 0, 7])))
