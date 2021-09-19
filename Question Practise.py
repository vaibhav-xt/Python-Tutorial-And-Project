""" 1. Write a program that inputs two tuples and creates a third that contains all elements of the first followed by
       all elements of the second. (you may user other data types such as list etc to make you program work)"""
"""
s = set()
tuple1 = (1, 3, 4, 5, 6)
tuple2 = (9, 87, 7, 56, 7, 0)
a = s.union(tuple1, tuple2)
print(a)
"""

""" 2. Write a program that accepts at least and removes the value at index 0 from the list. The program must actually
       modify the list passed in, and not just create a second list with the first item removed. You may assume the list 
       you are given, will have at least one element."""
"""
lst = [1, 3, 5, 6, 7, 8, 9]
lent = len(lst)
if lent == 0:
    print("List must contain one value.")
else:
    a = lst.remove(lst[0])
    print(lst)
"""

""" 3. Write a code a Python dictionary(the dict type) similar to previous question. Add three names and their phones
       in the dictionary after getting input from user. The names should act as keys and phones as their values. Then
       ask the user a name and print its corresponding phone."""
"""
dict = {"Rahul": 4542543, "Aman": 5874123, "Ram": 886663}
print("Enter Name To Know The PhoneNumber")
n = input("Enter The Name:")
if n in dict:
    print(f"{n}: {dict[n]}")
"""

""" 4. Given a dictionary with 5 students and their marks. Write a program that prints the dictionary contents
      in the ascending order of marks."""
"""
dict = {"Rahul": 50, "Ram": 60, "Rohit": 40, "Umang": 95, "Akul": 85}
"""

""" 5. Define a Python function called absolute that takes one parameter (x) and returns the absolute value of x, i.e., 
       as shown below: |x| = (x if x >= 0, -x otherwise).
       Don't forget to use a return statement at the end.
       Also, write the code that will demonstrate math absolute function by computing and print the absolute value of 6
       and -3. Be sure to pay attention to proper indentation."""
"""
import math
def function(x):


x = int(input("Enter the value of x: "))
print(function(x))
"""

""" 6. Write a program with a function chkOdd() that takes one argument (a positive integer) and reprots if the
       argument is odd or not."""
"""
def chkOdd(x):
    if x % 2 == 0:
        print("Number is not Odd.")
    else:
        print("Number is Odd.")

x = int(input("Enter Number To Check Weather it is Odd or not: "))
chkOdd(x)
"""

""" 7. Write a void function that receives a 4 digit number and calculates the sum of squares of first 2 digits number
       and last two digits number, e.g., if 1233 is passed as arguments then function should calculate 12 ** 3 + 33 ** 2
       ."""
"""
def void(x):
    lent = len(x)
    if lent == 4:
        if x.isnumeric():
            a = x[0] + x[1]
            a = int(a)
            b = x[2] + x[3]
            b = int(b)
            sum = a ** 2 + b ** 2
            print(sum)
        else:
            print("Enter Valid No.")
    else:
        print("Enter 4 Number Of Digits.")
x = input("Enter Number: ")
void(x)
"""

""" 8. Write a function that takes one argument (a positive integer) and reports if the argument is prime or not. 
      Write a program that invokes this function."""
"""
def prime(n):
    if (n == 1):
        return False
    elif (n == 2):
        return True
    else:
        for x in range(2, n):
            if (n %x == 0):
                return False
        return True

n = int(input("Enter Number: "))
print(prime(n))
"""

""" 9. Write a definition of method EvenSum(NUMBERS) to add those values is the list of NUMBERS, which are even."""
"""
def EvenSum(numbers):
    num = 0
    for number in (numbers):
        if number % 2 == 0:
            num = number + num
    print(num)

numbers = [1, 2, 3, 4, 56, 6, 7, 8]
EvenSum(numbers)
"""

""" 10. Write a method in python to find and display the prime number between 2 to N. Pas N as argument to the 
        method. """

def prime(value):
    if value > 2:
        for i in range(2, value):
            for j in range(2, i):
                if i % j == 0:
                    None
                else:
                    print(j)
        print("Are the prime numbers.")
    else:
        print("Value must be greater than 2.")

value = int(input("Enter the value: "))
prime(value)