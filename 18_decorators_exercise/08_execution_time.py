import time


def exec_time(func):
    def wrapper(*args):
        start = time.time()
        func(*args)
        end = time.time()
        difference = end - start
        return difference

    return wrapper


@exec_time
def loop():
    count = 0
    for i in range(1, 99999999):
        count += 1


print(loop())
