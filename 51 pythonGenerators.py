"""
Iterable - __iter__() or __getitem__()
Iterator - __next__()
Iteration -
"""
"""
def gen(n):
    for i in range(n):
        yield i

g = gen(5)
print(g)
# print(g.__next__())
# print(g.__next__())
# print(g.__next__())
# print(g.__next__())
# print(g.__next__())
# print(g.__next__())
"""

#fibonacci

def fac(f):
    if f == 1:
        yield 0
    elif f == 0:
        yield 1
    else:
        yield fac(f - 1) + fac(f - 2)

n = int(input("Enter Number: "))
a = fac(n)
print(a)
print(a.__next__())