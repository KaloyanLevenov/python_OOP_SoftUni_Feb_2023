def genrange(start, end):
    while start <= end:
        number = start
        yield number
        start += 1
