
# -------------------------Map Function--------------------------------

number = ["4", "3", "45"]
"""
for i in range(len(number)):   # We can do this in one line method see below
    number[i] = int(number[i])
"""
# numbers = list(map(int, number))  # Now we have to list here because map return object so we have to convert it.
#
# number[2] = number[2] + 1
# print(number[2])
"""
def fa(x):
    return x ** 2

lst = [1, 3, 5, 6, 78, 4, 3, 67]
square = list(map(fa, lst))
print(square)
"""
# above we have use def function to to print square now we use second method
"""
lst = [1, 34, 5, 6, 7, 4, 3, 65]
square = list(map(lambda x: x ** 2, lst))
print(square)
"""
"""
def square(a):
    return a * a

def cube(a):
    return a * a * a

func = [square, cube]
for i in range(5):
    var = list(map(lambda x: x(i), func))
    print(var)
"""

# _____________________________________Filter Function__________________________
"""
list1 = [3, 5, 2, 4, 45, 46546, 4545, 232, 5, 6, 6]
def greater(num):
    return num > 5

greaters = list(filter(greater, list1))  # this also print object so we use list
print(greaters)
"""
# ---------------------------------Reduce Function-----------------------------

# list1 = [3, 4, 65]
# num = 0
# for i in list1:
#     num = num + i
# print(num)
"""
from functools import reduce

list = [2, 3, 4, 5, 6]
num = reduce(lambda x, y: x + y, list)
print(num)
"""