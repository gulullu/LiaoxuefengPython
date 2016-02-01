# coding=utf-8
from collections import Iterable
from collections import Iterator

d = {'a': 1, 'b': 2, 'c': 3}

for key in d:
    print(key)

for value in d.values():
    print(value)

for k, v in d.items():
    print(k, v)

for ch in 'ABC':
    print(ch)

a = isinstance('abc', Iterable)
b = isinstance([1, 2, 3], Iterable)
c = isinstance(123, Iterable)
print(a, b, c)

for i, value in enumerate(['A', 'B', 'C']):
    print(i, value)

for x, y in [(1, 2), (2, 4), (3, 9)]:
    print(x, y)

isIt1 = isinstance((x for x in range(10)), Iterator)
print(isIt1)

isIt2 = isinstance([], Iterator)
print(isIt2)

isIt3 = isinstance({}, Iterator)
print(isIt3)

isIt4 = isinstance('abc', Iterator)
print(isIt4)

isIt5 = isinstance(iter([]), Iterator)
print(isIt5)

isIt6 = isinstance(iter('abc'), Iterator)
print(isIt6)


def add(x, y, f):
    return f(x) + f(y)


print(add(-5, 6, abs))
