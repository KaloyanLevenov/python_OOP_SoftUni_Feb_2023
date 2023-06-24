def even_parameters(func):
    def wrapper(*args):
        number_filter = lambda x: isinstance(x, int)
        params_are_numbers = all(map(number_filter, args))
        if params_are_numbers and all([x % 2 == 0 for x in args]):
            return func(*args)
        else:
            return "Please use only even numbers!"

    return wrapper


@even_parameters
def multiply(*nums):
    result = 1
    for num in nums:
        result *= num
    return result


print(multiply(2, 4, 6, 8))
print(multiply(2, 4, 9, 8))