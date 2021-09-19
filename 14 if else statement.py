"""
var = 3
var1 = 56
var3 = int(input())
if var3 > var1:
    print("Greater")
elif var1 == var3:
    print("Equal")
else:
    print("Lesser")
"""
"""
lst = [1, 2, 3, 4]
print(5 in lst)  # as in list we can see that 5 is not there hence it return false.
if 1 in lst:
    print("Yes it is in list")
else:
    print("No its not in the list")
"""

""" 1) Write a program, enter the age of candidate and print that it is eligible for car driving of not."""
"""
a = int(input("What is your age: "))
if a == 18:
    print("Come to office. Where we decide you are eligible for driving or not.")
elif a < 18:
    print("oops! You are not eligible for Car driving.")
else:
    print("Congratulation! You are eligible for car driving.")
"""

""" 2) Design a calculator which will correctly solve all the problems except the following ones:
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

""" 3) Write a program to print sum of first 'n' natural numbers."""
"""
n = int(input("Enter a number:"))
s = 0
for i in range(1, n + 1):
    s = i + s
print("Sum of first", n, "natural number is", s)
"""

"""" 4) Write a program that uses exactly four for loop to print the sequence of letter below. 
        AAAAAAAAAABBBBBBBEEEEE"""
"""
for i in range(1, 11):
    print("A", end="")
for r in range(11, 19):
    print("B", end="")
for j in range(19, 25):
    print("E", end="")
"""
