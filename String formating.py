def print_formatted(number):
    space = len(bin(number)[2:])

    for i in range(1, number + 1):
        print(*[str(i).rjust(space),
                oct(i)[2:].rjust(space),
                hex(i)[2:].upper().rjust(space),
                bin(i)[2:].rjust(space)])


