# coding=utf-8

L = [x * x for x in range(10)]
print(L)

g = (x * x for x in range(10))
print(g)

for n in g:
    print(n)


def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'


f = fib(6)
print(f)

for x in f:
    print(x)


def odd():
    print('step 1')
    yield 1
    print('step 2')
    yield 3
    print('step 3')
    yield 5


ge = fib(6)

while True:
    try:
        x = next(ge)
        print('g:', x)
    except StopIteration as e:
        print('Generator return value:', e.value)
        break
