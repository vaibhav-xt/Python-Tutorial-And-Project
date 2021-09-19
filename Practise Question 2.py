""" 1) Write a program to input some numbers repeatedly and print their sum. The program ends when the user says
       no more to enter (normal termination). The program aborts if a negative number is entered."""
"""
count = sum = 0
ans = "y"
while ans == "y":
    i = int(input("Enter Numbers: "))
    if i < 0:
        print("Number is negative.")
        break
    else:
        sum = sum + i
        count = count + 1
    ans = input("Want to enter more number? (y/n)")
print("You have entered all your number.")
print("Sum of numbers", sum)
"""

""" 2) Write a program to input any number and to check whether given is Armstrong or not. (An Armstrong number
       is a number digits then the sum of its digits raised to the nth power is equal to the number it-self. e.g.,
       371 is an Armstrong number, since 3**3 + 7**3 + 1**3 = 371.)"""
"""
# Python program to check if the number is an Armstrong number or not

# take input from the user
num = int(input("Enter a number: "))

# initialize sum
sum = 0

# find the sum of the cube of each digit
temp = num
while temp > 0:
   digit = temp % 10
   sum += digit ** 3
   temp //= 10

# display the result
if num == sum:
   print(num, "is an Armstrong number")
else:
   print(num, "is not an Armstrong number")
"""

""" 3) Write a program to check whether given number is composite or prime."""
"""
while True:
    n = int(input("Enter Number: "))
    if n > 1:
        for i in range(2, int(n / 2) + 1):
            if (n % i == 0):
                print(n, "is not a prime number.")
                break
        else:
            print(n, "is a prime number.")
    else:
        print(n, "is not a prime number.")
"""

""" 3) Write a program to convert binary to decimal."""
"""
b_num = list(input("Input a binary number: "))
value = 0
for i in range(len(b_num)):
    digit = b_num.pop()
    if digit == '1':
        value = value + pow(2, i)
print("The decimal value of the number is", value)
"""

""" 4) Write a program to input marks in 3 subjects; compute average and then calculate grade as per following 
       guidelines."""
"""
print("Input Marks in 3 subjects")
a = int(input("English:"))
b = int(input("Hindi:"))
c = int(input("Maths:"))
percent = ((a + b + c) / 300) * 100
if percent >= 80:
    print("A Grade, Percentage is", percent)
elif 70 < percent < 80:
    print("B Grade, Percentage is", percent)
elif 60 < percent < 70:
    print("C Grade, Percentage is", percent)
elif 50 < percent < 60:
    print("D Grade, Percentage is", percent)
elif 40 < percent < 50:
    print("E Grade, Percentage is", percent)
else:
    print("R Grade, Percentage is", percent)
"""

""" 5) Write a program that uses exactly four  for loops to print the sequence of letters below.
       AAAAAAAAAABBBBBBBCCCCCCEEEEE"""
"""
n = 65
s = 0
for i in range(11):
    p = chr(65)
    print(p, end="")
for j in range(11, 18):
    q = chr(n + 1)
    print(q, end="")
for r in range(18, 25):
    h = chr(n + 2)
    print(h, end="")
for r in range(25, 31):
    z = chr(n + 4)
    print(z, end="")
"""

""" 6) Write a program that checks in the range 1....100 and prints "Fizz" if the number is multiple of 3 and prints
       "Buzz" if the number is multiple of 5. It should print "FizzBuzz" if the number multiple of both 3 and 5."""
"""
n = 100
for i in range(1, 100):
    if i % 3 == 0:
        print("Fizz, and the Number is", i)
    elif i % 5 == 0:
        print("Buzz and the Numbers is", i)
    elif i % 3 == 0 and i % 5 == 0:
        print("Fizz Buzz and the Number is", i)
"""

""" 7) Use a for loop to print an upside down triangle like the one below. Allow the user to specify how high the
       triangle should be.
       * * * *
       * * *
       * *
       * """
"""
n = int(input("Enter Number of Rows: "))
for i in range(n, 0, -1):
    print("*" * i)
"""

""" 8) Write a script to print the following:
      8
      86
      864
      8642 """
"""
for i in range(8, 0, -2):
    for j in range(8, i - 1, -2):
        print(j, end="")
    print()
"""

""" 9) Write a Python script to print sum of negative numbers, sum of positive even numbers, sum of positive odd numbers
       from a list of numbers entered by the suer. The script should end when the number entered is zero."""
"""
list1 = []
n = int(input("Enter! How many numbers want to print in list (must be 30 numbers in list)?:"))
s = 0
for i in range(n + 2):
    if i == (n + 1):
        print(list1)
    else:
        s = -20 + i
        v = str(s)
        list1.append(s)
        continue
lent = len(list1)
print("Numbers Added Successfully In List")
print("Want to Print:-\n 1. Sum of Negative Numbers\n 2. Sum of Positive Even Numbers\n 3. Sum of Positive Odd Numbers")
choice = input("Enter Your Choice: ")
if choice == 1:
    r = 0
    for j in lent:
        if j < 0:
            r = r + j
            print("Sum of Negative Numbers:- ", r)
elif choice == 2:
    r = 0
    for j in lent:
        if j > 0 and j % 2 == 0:
            r = r + j
            print("Sum of Positive Even Numbers:- ", r)
elif choice == 3:
    r = 0
    for j in lent:
        if j > 0 and j % 2 != 0:
            r = r + j
            print("Sum of Positive Even Numbers:- ", r)
"""

""" 9) Take an integer input N from the user. Print N Fibonacci numbers. Recall that Fibonacci series progresses 
       as 0 1 1 2 3 5 8 13...  """
"""
def fac(f):
    if f == 1:
        return 0
    elif f == 0:
        return 1
    else:
        return fac(f - 1) + fac(f - 2)
n = int(input("Enter number"))
print(fac(n))
"""