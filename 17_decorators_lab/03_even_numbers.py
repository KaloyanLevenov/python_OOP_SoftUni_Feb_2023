def even_numbers(function):

    def wrapper(numbers):
        input_data = function(numbers)
        result = [number for number in input_data if number % 2 == 0]
        return result

    return wrapper


@even_numbers
def get_numbers(numbers):
    return numbers


print(get_numbers([1, 2, 3, 4, 5]))
