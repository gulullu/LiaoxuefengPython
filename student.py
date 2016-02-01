#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" a test student """


class Student(object):
    """ a test student """

    def __init__(self, name, score):
        self.name = name
        self.score = score

    def print_score(self):
        print('%s: %s' % (self.name, self.score))

    def get_grade(self):
        if self.score >= 90:
            return 'A'
        elif self.score >= 60:
            return 'B'
        else:
            return 'C'


bart = Student('Bart Simpson', 59)
# bart.name = 'Bart Simpson'
bart.print_score()
print(bart.get_grade())
print(bart.name)
print(Student)
