#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" a test partial """
import functools

int2 = functools.partial(int, base=2)
print(int2('1000000'))
