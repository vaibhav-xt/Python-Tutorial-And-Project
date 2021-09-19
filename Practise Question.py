""" 1) Write a program to read a number. If the number is even print half the number otherwise print the next number.
       End your program by printing "Thank You". """
"""
n = int(input("Enter Value: "))
if n % 2 == 0:
    print(n, "is even")
    print(n/2, "is even and half the number of", n)
else:
    print(n, "is odd number.")
    print("So", n + 1, "is the next number.")
print("Thank You")
"""

""" 2) Write a program to print negative, zero or positive according to whether variable x is less than zero,
    or greater than zero respectively"""
"""
q = int(input("Enter value: "))
if n > 0:
    print(q, "is greater than zero.")
elif n == 0:
    print(q, "is equal to zero.")
else:
    print(q, "is negative")
"""

""" 3) Write a program that accepts two integers from the user and prints a message saying it first number is divisible
    by second number of if it is not. """
"""
a = int(input("Enter integer: "))
b = int(input("Enter second integer"))
if a % b == 0:
    print("First number is divisible by second number.")
else:
    print("First numbers is not divisible by second number.")
"""

""" 4) Write a program to display a menu for calculating area of a circle and perimeter of a circle."""
"""
radius = float(input("Radius is: "))
print("1. Calculate Area")
print("2. Calculate Perimeter")
choice = int(input("Enter your choice 1 or 2: "))
if choice == 1:
    area = 3.14 * radius ** 2
    print("Area of circle is ", area)
elif choice == 2:
    perimeter = 2 * 3.14 * radius
    print("Perimeter of circle is:", perimeter)
else:
    print("Choice is wrong.")
print("** Thanks To use Calculator **")
"""

""" 5) Write a program to input username and password and to check whether
       the given username and password are correct or not. """
"""
import string
username = raw_input("Enter Username: ")
password = raw_input("Enter Password: ")
if cmp(username.strip(), "XXX") == 0:
    if cmp(password, "123") == 0:
        print("Login successful")
    else:
        print("Password Incorrect")
else:
    print("Username Incorrect")
"""

""" 6) Write a program that reads three numbers and print them in ascending oder."""
"""
x = int(input("Enter first number"))
y = int(input("Enter second number"))
z = int(input("Enter third number"))
asc = [x, y, z]     # using list 
asc.sort()
print(asc)
"""
# alternate method
"""
while True:
    x = int(input("Enter first number"))
    y = int(input("Enter second number"))
    z = int(input("Enter third number"))
    if x < y and x < z:
        if y < z:
            f, s, t = x, y, z
        else:
            f, s, t = x, z, y
    elif y < x and y < z:
        if x < z:
            f, s, t = y, x, z
        else:
            f, s, t = y, z, x
    else:
        if x < y:
            f, s, t = z, x, y
        else:
            f, s, t = z, y, x
    print("Numbers in ascending order are", f, s, t)
"""

""" 7) Write a program to calculate and print roots of a quadratic equation ax**2 + bx + c = 0."""
"""
import math
print("Enter Coefficients of the equation.")
a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))
if a == 0:
    print("Value a should not be zero.")
else:
    x = b ** 2 - 4 * a * c
    if x > 0:
        r1 = (-b + math.sqrt(x)) / (2 * a)
        r2 = (-b - math.sqrt(x)) / (2 * a)
        print("Roots are: ", r1, r2)
    elif x == 2:
        r1 = -b / (2 * a)
        print("Roots are equal", r1)
    else:
        print("Roots are complex and imaginary")
"""

""" 8) A student will not be allowed to sit in exam if his/her attendance is less than 75%. Take following input from user,
       Number of classes held, Number of classes attended. And print percentage of class attended . Is student allowed to 
       sit in exam or not."""
"""
print("**** **Enter Details of student** ****")
a = int(input("Enter Number of classes held: "))
b = int(input("Enter Number of classes attended: "))
p = (b / a) * 100
if a == 0:
    print("Number of classes held does not equal to zero.")
else:
    if p > 75:
        print("Student is eligible for exam. His/Her percentage of attendance is: ", p, "%.")
    else:
        print("Student is not eligible for exam. His/Her percentage of attendance is: ", p, "%.")
"""

""" 9) Take input of age of 3 people by user and determine oldest and youngest among them."""
"""
print("Input Age of Users")
a = int(input("Enter the age of first person: "))
b = int(input("Enter the age of second person: "))
c = int(input("Enter the age of third person: "))
if a < b and a < c:
    if b < c:
        d, e, r = a, b, c
        print("Youngest person is ", d, ". Oldest person is ", r, ".")
    else:
        d, e, r = a, c, b
        print("Youngest person is ", d, ". Oldest person is ", r, ".")
elif b < a and b < c:
    if a < c:
        d, e, r = b, a, c
        print("Youngest person is ", d, ". Oldest person is ", r, ".")
    else:
        d, e, r = b, a, c
        print("Youngest person is ", d, ". Oldest person is ", r, ".")
elif c < a and c < b:
    if a < b:
        d, e, r = c, a, b
        print("Youngest person is ", d, ". Oldest person is ", r, ".")
    else:
        d, e, r = c, b, a
        print("Youngest person is ", d, ". Oldest person is ", r, ".")
else:
    print("All are equal.")
"""

""" 10) Write a program to accept a number n from the user and print its table."""
"""
n = int(input("Enter number you want table of: "))
for i in range(1, 10):
    a = n * i
    print(n, "*", i, "=", a)
"""

""" 11) Write a program to create a dictionary and take input form the user and return the meaning 
        of the word from the dictionary."""
"""
print("Word in Dictionary are:-\n Mutable\n Immutable\n Set\n Tiny")
a = input("Enter word you want meaning of ")
d = {"Mutable": "can change", "Immutable": "can't change", "Set": "a collection of set", "Tiny": "Little"}
print("Meaning of ", a, "is", d[a])
"""
# alternate method
"""
dic1={"key":"something which unlocks a lock",
      "book":"a compiled set of pages which describes a certain topic",
      "comb":"a plastic item to set hairs",
      "mouse":"an animal which is afraid of cats",
      "joey":"kid of a kangaroo"}
print("Please enter the word whose meaning you want")
ax=input()
print(dic1[ax])
"""

""" 12) Write a program, enter the age of candidate and print that it is eligible for car driving of not."""
"""
a = int(input("What is your age: "))
if a == 18:
    print("Come to office. Where we decide you are eligible for driving or not.")
elif a < 18:
    print("oops! You are not eligible for Car driving.")
else:
    print("Congratulation! You are eligible for car driving.")
"""

""" 13) Design a calculator which will correctly solve all the problems except the following ones:
        addition, multiplication, division. Your program should take operator and the two numbers as input from
        the user and then return the result."""
"""
print("Enter the Method you want :-\n 1.Addition\n 2.Subtraction\n 3.Division\n 4.Multiplication")
choice = int(input("Enter your choice: "))
if choice < 5:
    a = int(input("Enter the first value: "))
    b = int(input("Enter the second value: "))
    if choice == 1 and a + b:
        print(a, "+", b, "=", 77)
    elif choice == 2 and a - b:
        print(a, "-", b, "=", a - b)
    elif choice == 3 and a / b:
        print(a, "/", b, "=", 4)
    elif choice == 4 and a * b:
        print(a, "*", b, "=", 555)
else:
    print("You have entered wrong choice.")
"""

""" 14) Write a program to print sum of first 'n' natural numbers."""
"""
n = int(input("Enter a number:"))
s = 0
for i in range(1, n + 1):
    s = i + s
print("Sum of first", n, "natural number is", s)
"""

""" 15) Write a program that uses exactly four for loop to print the sequence of letter below. 
        AAAAAAAAAABBBBBBBEEEEE"""
"""
for i in range(1, 11):
    print("A", end="")
for r in range(11, 19):
    print("B", end="")
for j in range(19, 25):
    print("E", end="")
"""

""" 16) Write a program that print a list of the integers from 1 to 20 and their squares.
        The output should look like this
        1----1
        2----2
        -----
        20----400"""
"""
for i in range(1, 21):
    print(i, "----", i ** 2)
"""

""" 17) Convert the following for loop into while loop.
        for i in range(1,100,1):
            if i % 4 == 2:
                print(i, "mod", 4, "= 2")"""
"""
i = 1
while i < 100:
    if i % 4 == 2:
        print(i, "mod", 4, "= 2")
    i = i + 1
"""

""" 18) Write a Python program to print the following pyramid:
        A
        BB
        CCC
        DDDD
        EEEEE """
"""
n = int(input("Enter a number of n:"))
for i in range(n):
    print((chr(65 + i)) * (i + 1))
"""

""" 18) Write a program to input any number and print all the factors of that number."""
"""
n = int(input("Input number: "))
for i in range(1, n + 1):
    if n % i == 0:
        print("The factor of", n, "is", i)
"""

""" 19) Write a program to find the sum of all digits of the given numbers."""
"""
n = int(input("Input the number you want the sum of digits: "))
s = 0
while n > 0:
    a = n % 10
    s = s + a
    n = n // 10
print("Sum of digits =", s)
"""

""" 20) Write a program to find the reverse of the number."""
"""
number = int(input("Input Value: "))
revs_number = 0
while (number > 0):
    remainder = number % 10
    revs_number = (revs_number * 10) + remainder
    number = number // 10
print("The reverse number is: ", revs_number)
"""

""" 21) Write a program to print the pyramid:
        1
        22
        333
        4444"""
"""
for i in range(1, 6):
    for j in range(1, i + 1):
        print(i, end="")
    print()
"""