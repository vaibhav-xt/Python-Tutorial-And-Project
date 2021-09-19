
                             # TABLE OF ANY NUMBER

# First Method
"""
a = int(input("Enter number you want table of: "))
s = 1
for i in range(1, 11):
    d = s * a
    s = s + 1
    print(d)
"""

# SECOND METHOD
"""
a = int(input("Enter number you want table of: "))
s = 0
while a != 0:
    s = s + 1
    d = s * a
    if s == 10:
        print(d)
    else:
        continue
"""

                                  # PROGRAM
"""
n = int(input("Enter number"))
s = 1
for i in range(1, 6):
    d = n ** s
    s = s + 1
    print(d, end="  ")
"""
"""
r = int(input("Enter radius of sphere: "))
d = 3.14
s = 4 * d * r ** 2
v = 4 / 3 * d * r **3
print("Surface area of sphere is ", s, "and Volume of the sphere is ", v)
"""

                        # calculator to calculate height in inch or feet
"""
n = int(input("Enter your height:"))
inch = n / 2.54
foot = inch / 12
print("In inch you height is ", inch, "inch.", "In foot you height is ", foot, "feet")
"""
"""
height = int(input("Enter the height of the triangle"))
base = int(input("Enter the base of the triangle"))
a = 1/2 * base * height
print("The Height and Base of the triangle is ", height, ",base is ", base, " respectively. Area of the triangle is", a)
"""

                     # find quotient and remainder
"""
a = int(input("Enter the value"))
b = int(input("Enter the second value"))
q = a / b
r = a % b
print("The quotient is ", q, "and the remainder is ", r)
"""

                    # compute simple interest and compound simple interest
"""
p = int(input("Enter principal amount"))
r = int(input("Enter rate of interest"))
t = int(input("Enter time period"))
SI = p * r * t / 100
CI = p * (1 + r / 100) ** t - p
print("Simple Interest is ", SI, "Compound Interest", CI)
"""
