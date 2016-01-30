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


Solver().demo(2.0, 3.0, 6.0)
