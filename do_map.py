# coding=utf-8
from functools import reduce


def f(x):
    return x * x


r = map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])
print(list(r))

s = map(str, [1, 2, 3, 4, 5, 6, 7, 8, 9])
print(list(s))


def add(x, y):
    return x + y


print(reduce(add, [1, 3, 5, 7, 9]))


def fn(x, y):
    return x * 10 + y


def char2num(s):
    return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]


print(reduce(fn, [1, 3, 5, 7, 9]))
print(reduce(fn, map(char2num, '13579')))


# def str2int(s):
#     def fn(x,y):
#         return x * 10 +y
#     def char2num(s):
#         return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]
#     reduce(fn, map(char2num, s))

def str2int(s):
    return reduce(lambda x, y: x * 10 + y, map(char2num, s))
