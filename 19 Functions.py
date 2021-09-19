"""
# built in function
a = 0
b = 5
# c = sum (a, b) Here guys this comment not run because sum works when you insert tuple or list see below
c = sum((a, b))
print(c)
"""
# user defined function
"""
def function1(a, b):
    print("Hello Python.", a + b)
# print(function1())  it return none value
function1(1, 21)
function1(1, 3)
function1(3, 45)
"""
"""
def function2(b, c):
    average = (c + b)/2
    print(average)
    return average   # if we don't write return function then the value
                     # we have assign to v return none. so we have to use it.
function2(5, 7)
v = function2(5, 5)
print(v)
"""

# how to print doc string.
        # Doc string is written to uderstand about fucntion when we use fucntion in program
        # for our convinience
def function2(b, c):
    """This is a function which will calculate average of two number"""
    average = (c + b)/2
    print(average)
    return average
print(function2.__doc__)