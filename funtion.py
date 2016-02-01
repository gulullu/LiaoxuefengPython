# coding=utf-8

import math

a = abs(100)
print(a)
b = abs(-20)
print(b)

c = abs
print(c(-2))


def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x


print(my_abs(-10))


def nop():
    pass


if a >= 18:
    pass


# my_abs('10')


def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny


x, y = move(100, 100, 60, math.pi / 6)
print(x, y)


def power(x, n=2):
    s = 1
    while n > 0:
        n -= 1
        s *= x
    return s


print(power(5))
print(power(16))


def enroll(name, gender, age=6, city='Beijing'):
    print('name:', name)
    print('gender:', gender)
    print('age:', age)
    print('city', city)


enroll('Sarah', 'F')
enroll('Bob', 'M', 7)
enroll('Adam', 'M', city='Tianjin')


def add_end(L=None):
    if L is None:
        L = []
    L.append('END')
    return L


# print(add_end([1, 2, 3]))
print(add_end())
print(add_end())


def calc(*numbers):
    sum = 0
    for n in numbers:
        sum += n * n
    return sum


print(calc(1))
print(calc(1, 2, 3))

nums = [1, 2, 3]
print(calc(*nums))


# def person(name, age, **kw):
#     print('name:', name, 'age:', age, 'other:', kw)
#
#
# print(person('Michael', 30))
# print(person('Allen', 45, city = 'Beijing'))
# print(person('Zhang', 20, birth= 15, job = 'iOS'))
#
# extra = {'city': 'Beijing', 'job': 'Engineer'}
# print(person('Amy', 45, **extra))

def person(name, age, *, city='Beijing', job):
    print(name, age, city, job)


print(person('Jack', 24, job='Engineer'))


def f1(a, b, c=0, *args, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)


def f2(a, b, c=0, *, d, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)


def fact(n):
    return fact_iter(n, 1)


def fact_iter(num, product):
    if num == 1:
        return product
    return fact_iter(num - 1, num * product)


print(fact(5))
print(fact(100))
print(fact(1000))
