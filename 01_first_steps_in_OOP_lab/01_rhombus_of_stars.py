"""Create a program that reads a positive integer N as input and prints on the console a rhombus with size n:"""


def choice_pattern():
    pattern = input('Choice type of pattern ->\n- Rombus\n- Sand Clock\nYour choice: ')
    size = int(input('Enter pattern size: '))
    return pattern, size


def print_func(space, stars):
    print(' ' * space + '* ' * stars)


def data_pattern(pattern, size):
    if pattern == 'Rombus':
        for x in range(size):
            space_data = size - (x + 1)
            star_data = x + 1
            print_func(space_data, star_data)

        for x in range(size - 1, -1, -1):
            space_data = size - x
            star_data = x
            print_func(space_data, star_data)
    elif pattern == 'Sand Clock':
        for x in range(size):
            space_data = x
            star_data = size - x
            print_func(space_data, star_data)

        for x in range(size - 1):
            space_data = size - (x + 2)
            star_data = x + 2
            print_func(space_data, star_data)


data_pattern(*choice_pattern())
