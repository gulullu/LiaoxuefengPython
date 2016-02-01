#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" a test module """

import sys


def test():
    """ a test module """
    args = sys.argv
    if len(args) == 1:
        print('Hello, World!')
        print(__doc__)
    elif len(args) == 2:
        print('Hello, %s!' % args[1])
    else:
        print('Too many arguments!')


def _private_1(name):
    return 'Hello, %s' % name


def _private_2(name):
    return 'Hi, %s' % name


def greeting(name):
    """ a test private """
    if len(name) > 3:
        return _private_1(name)
    else:
        return _private_2(name)


if __name__ == '__main__':
    test()
