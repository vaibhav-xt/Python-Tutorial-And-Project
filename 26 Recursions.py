# Recurions means function in function

# iterative method
"""
def factorial(n):
        fac = 1
        for i in range(n):
             fac = fac * (i + 1)
        return fac
number = int(input("Enter the number"))
print(factorial(number))
"""
"""
# recursive method
def factorial_recersive(n):
        if n == 1:
                return 1
        else:
                return n * factorial_recersive(n - 1)

number = int(input("Enter the number"))
print("Factorial using recursive method", factorial_recersive(number))
"""
# calculate fibonacci sequence e.g 0 1 1 2 3 5 8 13
def fac(f):
       if f == 1:
               return 0
       elif f == 0:
               return 1
       else:
               return fac(f - 1) + fac(f - 2)
n = int(input("Enter number"))
print(fac(n))