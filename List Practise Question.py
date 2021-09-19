""" 1. Write a program that prints the sum of the even-indexed elements of L, minus the sum of the odd-indexed elements
       of L."""
import string

"""
l = 76
i = chr(76)
print("ASCII code of 76 is ", i)
s = 0
sum = 0
for i in range(1, 77):
    if i % 2 == 0:
        s = s + i
    else:
        sum = sum + i
total = s - sum
print("Even Sum is", s)
print("Odd Sum is", sum)
print("The sum of even-indexed minus odd-indexed is ", total)
"""

""" 2. Write a program that returns the largest even number in the list of integers. If there is no even number in
       the input, print "No Even Element". """
"""
lst = [1, 5, 3, 23, 57]
lst1 = []
for i in lst:
    if i % 2 == 0:
        lst1.append(i)
    else:
        continue
if len(lst1) == 0:
    print("No Even Element.")
else:
    print(max(lst1), "is the Largest Element.")
"""

""" 3. Write a program to find the median from a given list, e.g. if the given list is:
       23, 9, 14, 2, 28, 19, 3, 15, 9, 25, 2, 4, 9."""
"""
lst = [23, 9, 14, 2, 28, 19, 3, 15, 9, 25, 2, 4, 9]
n = len(lst)
print(lst)
median = int(n / 2)
print("Median is", lst[median - 1])
"""

""" 4. Write program th find the mod, form a given list e.g., if the given list is 
       23, 9, 14, 2, 28, 19, 3, 15, 9, 25, 2, 4, 9. """
"""
import statistics
lst = [23, 9, 14, 2, 28, 19, 3, 15, 9, 25, 2, 4, 9]
mode = statistics.mode(lst)
print("Mode is", mode)
"""

""" 5. Write a program to find the range, form a given list, e.g., if the given list is:
       23, 9, 14, 2, 28, 19, 3, 15, 9, 25, 2, 4, 9. Hint:- Range is the difference between the largest nad lowest
       number. In this case largest is 28 and lowest is 2. So 29 - 2 = 0"""
"""
lst = [10, 20, 30, 40, 50, 40, 40, 60, 70]
lst.sort()
print(lst)
lent = len(lst)
lent = lent - 1
if len(lst) != 0:
    a = lst[lent] - lst[0]
    print("Range is: ", a)
else:
    print("List is empty.")
"""

""" 6. Write a program to print letters form the English alphabet from a-z and A-Z."""
"""
import string
print("Alphabet from a-Z:")
for letter in string.ascii_letters:
    print(letter, end=" ")
print("\nAlphabet from a-z:")
for letter in string.ascii_lowercase:
    print(letter, end=" ")
print("\nAlphabet form A-Z:")
for letter in string.ascii_uppercase:
    print(letter, end=" ")
"""

""" 7. Cumulative sum of a list [a, b, c,....] is defined as [a, a+b, a+b+c,..]. Write a program to input a list
       of number and then create another list form this that contains cumulative sum of numbers in list1."""
"""
lst = []
for letter in string.ascii_uppercase:
    lst.append(letter)
print(lst)
lst1 = []
s = ""
for i in lst:
    if i == "A":
        s = s + i
        lst1.append(s)
    else:
        s = s + "+" + i
        lst1.append(s)
print(lst1)
"""

""" 8. Given a list of strings L, write a program below that print a single a string containing all of the elements of
       L concatenated together with a hyphen in between two elements."""

L = eval("Input Sentence:")
lent = len(L)
strings = ""
for i in L:
    if i == L[0]:
        strings = strings + i
    else:
        stings = strings + "-" + i
print(strings)


