# coding=utf-8
"""ds"""
import math


class Solver(object):
    """jds"""

    def demo(self, a, b, c):
        """

        :param a:
        :param b:
        :param c:
        :type a: float
        :type b: float
        :type c: float
        :return: float
        """
        d = b ** 2 - 4 * a * c
        if d >= 0:
            disc = math.sqrt(d)
            root1 = (-b + disc) / (2 * a)
            root2 = (-b - disc) / (2 * a)
            print(root1, root2)
            return root1, root2
        else:
            raise Exception


# s = input('birth:')
# birth = int(s)
# if birth < 2000:
#     print('00前')
# else:
#     print('00后')
#
# names = ['Michael', 'Bob', 'Tracy']
# for name in names:
#     print(name)


# sum = 0
# for x in range(101):
#     sum += x
# print(sum)

sum = 0
n = 99
while n > 0:
    sum += n
    n -= 2
print(sum)

d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
print(d['Michael'])
