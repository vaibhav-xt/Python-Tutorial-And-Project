"""
l = 10  # Global Variable
def funtion1(n):
    # print(l)    # it print global variable
    # l = 5   # local variable
    m = 7   # local
    global l
    l = l + 1  # here l value can't change because l is global if we use local variable then it will.
               # if we want to give permission to global variable the we have to write in function "global l see below"
    print(l, m)
    print(n, "I have printed.")
funtion1("This is me")
# print(m)  # m can't print because m is in def function1
"""
x = 89
def harry():
    x = 20
    def rohan():
        global x
        x = 88
    print("before calling rohan()", x)
    rohan()
    print("after calling rohan()", x)
harry()
print(x)