def multiply(times):
    def decorator(function):
        def wrapper(num):
            return times * (function(num))

        return wrapper

    return decorator


@multiply(5)
def add_ten(number):
    return number + 10

print(add_ten(6))


print(multiply(10))