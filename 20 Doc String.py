# how to print doc string.
        # Doc string is written to uderstand about fucntion when we use fucntion in program
        # for our convinience
def function2(b, c):
    """This is a function which will calculate average of two number"""
    average = (c + b)/2
    print(average)
    return average
print(function2.__doc__)