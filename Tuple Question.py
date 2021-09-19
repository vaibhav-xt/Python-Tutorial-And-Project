""" 1. Write a program to print every 3rd element of a tuple T, raised t power 3. """
"""
t = (1, 2, 4, 5, 6, 7, 3, 54, 23, 9)
lent = len(t)
print(lent)
i = 0
for i in t:
"""

""" 2. Write a program that inputs a tuple having words of a string as its elements e.g., ("The", "quick", "brown", 
       "fox") and then translates each text element to Pig Latin.
       [English is translated to Pig Latin by taking the first letter of every word, moving it to the end of the word 
       and adding 'ay'. "The quick brown fox" becomes "Hetay uickqay rownbay oxfay".]"""
"""
t = ("The", "quick", "brown", "fox")
for i in t:
    lent = len(i)
    a = i.removeprefix(i[0])
    b = i.removesuffix(i[lent - 1])
    c = a + b
    print(a)
"""

""" 3. Write a program that inputs a tuple T and prints a tuple of the lengths of the sub tuples. For example, if passed
       tuple T is ((1, 2), (2, 4, 6), (4, ), (5, 0, 5)) then is should prints (2, 3, 1, 3)"""
"""
tup = ((1, 2), (2, 4, 6), (4, ), (5, 0, 5))
for i in tup:
    lent = len(i)
    print(lent, end=", ")
"""

""" 4. Write a program that inputs a number n(integer) and creates a tuple containing: n, 2n, 3n and 4n. """
"""
b = int(input("Enter No. Integer: "))
t = tuple()
for i in range(0, b + 1):
    t = tuple("n")
    print(t, end="")
"""
""" 5. Write a program that uses a dictionary that contains ten username and passwords. The program should alk the user
       to enter their username and passwords. If the username is not in the dictionary, the program should indicate
       that the person is not a valid user of the system. If the username is in the dictionary, but the user does
       not enter the right password, the program should say that the password is invalid. If the password is correct,
       then the program should tel the user that they are now logged into the system."""
"""
while True:
    print("** * Want To Logged Into The System * **")
    print("Enter Your Username and Password to Login into System:-\n 1. Login\n 2. Exit")
    choice = input("Enter You Choice: ")
    if int(choice) == 1:
        dic = {"Rohan": 54216, "Harsh": 5437, "Vaibhav": 8858, "Ram": 67432, "Rohit": 12345, "Gupta": 67890,
        "Hat": 3426, "Raj": 34234, "Gun": 3416, "Pin": 34232}
        userinput = input("Enter Username: ")
        userinput = userinput.capitalize()
        if userinput in dic:
            userpin = int(input("Enter User pin: "))
            if userpin == dic[userinput]:
                print("You are now logged into the system.\n")
            else:
                print("Password is inValid.\n")
        else:
            print("Username is inValid.\n")
    elif int(choice) == 2:
        break
    else:
        print("Entered wrong choice!\n")
"""

""" 6. Write a program to print following ASCII art using print statements: """
"""
print("        ____________________")
print("       /                    \ ")
print("      /  /           \ \     \ ")
print("     |                        |")
print("    /                        /")
print("   |            ___\ \| | / /")
print("   |            /           |")
print("   |            |           |")
print("  /             |      __   |")
print("  |             |        \  |")
print("  |             |         \ | ")
print("  |            __\          |")
print("  |            |       __   |")
print("   \           |      ( o)  |")
print("    |          ||           |")
print("    |          |             \ ")
print("    |          |              \ ")
print("    |          |               \ ")
print("    |          |          (*____")
print("    |         /    -        |")
print("     \|      /   //_________|")
print("      |             |_|_|_|___/\ ")
print("      |            \ -         | ")
print("      |            _----______/")
print("      |           /"  )
print("      |          /")
"""

import math
a = math.fabs(545)
print(a)
