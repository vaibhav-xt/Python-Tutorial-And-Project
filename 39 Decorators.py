# def function1():
#     print("subscribe now")
#
# func2 = function1
# del function1
# func2()

# we can print function als0
"""
def funcret(num):
    if num == 0:
        return print
    if num == 1:
        return int

a = funcret(1)
print(a)
"""

# def executor(func):
#     func("this")
#
#
# executor(print)

#                       NOW DECORATORS

def dec1(func1):
    def nowexec():
        print("Executing Now")
        func1()
        print("Executed")
    return nowexec()
@dec1   # here @ denotes as the decrators
def work():
    print("Vaibhav is a good boy.")
# work = dec1(work)      # this method work as decorators
# work()
