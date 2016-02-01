# coding=utf-8

def calc_sum(*args):
    ax = 0
    for n in args:
        ax += n
    return ax


def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax

    return sum


f1 = lazy_sum(1, 3, 5, 7, 9)
f2 = lazy_sum(1, 3, 5, 7, 9)
print(f1)
print(f1())
print(f1 == f2)


def count():
    fs = []
    for i in range(1, 4):
        def f():
            return i * i

        fs.append(f)
    return fs


fs1, fs2, fs3 = count()
print(fs1())
print(fs2())
print(fs3())
