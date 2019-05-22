import math
import sys

kor_nums = ['영', '일', '이', '삼', '사', '오', '육', '칠', '팔', '구']
kor_digits = ['억', '만', '천', '백', '십']

kor_digit_dic = {'십': 10, '백': 100, '천': 1000, '만': 10000, '억': 100000000}
# kor_major_digit = {}


def sum(args: list):
    _validate_arguments(args)
    return _convert_to_kor(_convert_to_int(args[0]) + _convert_to_int(args[1]))


def _validate_arguments(args: list):
    if len(args) != 2:
        raise ValueError('arguments are invalid. args:{}'.format(args))

    for arg in args:
        _validate_integer(arg)


def _validate_integer(arg: str):
    for char in arg:
        if char in kor_nums:
            return True
        elif char in kor_digits:
            return True
        else:
            raise ValueError


def _convert_to_int(int_kor: str):
    num = 0

    length = len(int_kor)
    if length == 1:
        return _get_int(int_kor)

    if length == 2:
        num = _get_int(int_kor[0])
        if num % 10 == 0:
            return num + _get_int(int_kor[1])
        else:
            return num * _get_int(int_kor[1])

    if length >= 3:
        for digit in kor_digits:
            try:
                digit_i = int_kor.index(digit)
                if digit_i == 0:
                    num += _get_int(digit)
                else:
                    num_value = _convert_to_int(int_kor[:digit_i])
                    num += num_value * _get_int(digit)

                if digit_i < length:
                    num += _convert_to_int(int_kor[digit_i+1:])
                break
            except ValueError:
                continue

    return num


def _get_int(char: str):
    try:
        return kor_nums.index(char)
    except ValueError:
        return kor_digit_dic[char]


def _convert_to_kor(num: int):
    kor = ''
    if num == 0:
        return ''
    if num < 10:
        return kor_nums[num]

    for digit_kor in kor_digits:
        digit_val = _get_int(digit_kor)
        if num >= digit_val:
            num_kor = _convert_to_kor(int(math.floor(num/digit_val)))
            if num_kor == '일' or num_kor == '영':
                num_kor = ''
            kor += '{}{}'.format(num_kor, digit_kor)
            kor += _convert_to_kor(num%digit_val)
            break
        else:
            continue

    return kor


if __name__ == '__main__':
    args_ = sys.argv[1:]
    try:
        print(sum(args_))
    except ValueError as e:
        print(e)
        exit(1)
