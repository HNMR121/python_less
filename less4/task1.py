# argv обязательно

from sys import argv


def func(a, b, c):
    return ((int(a) * int(b)) + int(c))


print(func(argv[1], argv[2], argv[3]))
