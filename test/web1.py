from functools import reduce


def prod(l):
    def fn(x, y):
        return x*y

    return reduce(fn, l)


l1 = prod([1, 2, 3, 4, 5])
print(l1)
print(type(l1))



