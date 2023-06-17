def squares(number):
    for element in range(1, number + 1):
        yield element ** 2

print(list(squares(5)))