import math
import sys

ASCII_ZERO = 48
ASCII_NINE = 57


def sum_str(args: list):
    _validate_arguments(args)
    return _convert_to_int(args[0]) + _convert_to_int(args[1])


def _validate_arguments(args: list):
    if len(args) != 2:
        raise ValueError('arguments are invalid. args:{}'.format(args))

    for arg in args:
        _validate_integer(arg)


def _validate_integer(arg: str):
    for char in arg:
        if ord(char) < ASCII_ZERO or ord(char) > ASCII_NINE:
            raise ValueError('the argument is not number. {}'.format(arg))


def _convert_to_int(int_str: str):
    reverted_str = int_str[::-1]
    result = 0
    for i in range(len(int_str)):
        char = reverted_str[i]
        num = ord(char) - ASCII_ZERO
        if i == 0:
            result += num
        else:
            place = int(math.pow(10, i))
            result += num*place

    return result


if __name__ == '__main__':
    args_ = sys.argv[1:]
    try:
        print(sum_str(args_))
    except ValueError as e:
        print(e)
        exit(1)
