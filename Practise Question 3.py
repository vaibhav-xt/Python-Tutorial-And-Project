""" 1. Write a program to input n numbers and to search any numbers from the list."""
"""
n = int(input("Enter numbers of values: "))
list1 = []
s = 0
for i in range(n):
    userinput = int(input("Enter number: "))
    add = list1.append(userinput)
    s = i + s
search = int(input("Enter number you want to search: "))
for i in range(n):
    if list1[i] == search:
        print("Entered Number is found.")
        break
"""

""" 2. Write a program to search input any customer name and display customer phone number if the customer name exist 
       in the list."""
"""
def printlist(s):
    i=0
    for i in range(len(s)):
        print i,s[i] i = 0
        phonenumbers = [‘9840012345’,‘9840011111’,’  9845622222’,‘9850012345’,‘9884412345’]
        flag=0 number = raw_input("Enter the phone number to be searched")
        number = number.strip() try:
            i = phonenumbers.index(number)
            if i >= 0:
                flag=1
                except ValueError:
                pass if(flag <>0):
                    print("\nphone number found in Phonebook at index", i)
                    else:
                    print("\iphonenumbernotfoundin phonebook")
                    print “\nPHONEBOOK” printlist(phonenumbers)
"""

""" 3. Write a program that take a string with multiple words and the capitalizes the first letter of each word 
       and forms a new string out of it."""
"""
str = input("Enter String:")
s = len(str)
a = 0
if s > a:
    cap = str.capitalize()
    print(cap)
else:
    print("Nothing has been written by the user.")
"""

""" 4. Write a program that read a string and check whether it is a palindrome string or not."""
"""
str = input("Enter string:" )
if (str == str[::-1]):
    print("The string is palindrome.")
else:
    print("The string is not palindrome.")
"""

""" 5. Write a program that prompts for a phone number of 10 digits and two dashes with dashes after the area
       code  and the next thee numbers. e.g. 017-555-5643 is a legal input. Display if the phone number entered
       is valid format or not and display if the phone number is valid or not."""
"""
number = input("Enter Phone Number: ")
if len(number) == 12:
    if number[3] == "-" and number[7] == "-":
        if (number[:3] + number[4:7] + number[8: ]).isdigit():
            print("Phone Number is valid.")
else:
    print("Phone Number is not Valid.")
"""

""" 6. Print first 10 prime numbers. """
"""
lower = int(input("Enter the lower value:"))
upper = int(input("Enter the upper value:"))
for number in range(lower,upper+1):
    if number>1:
        for i in range(2,number):
            if (number%i)==0:
                break
        else:
            print(number)
"""
"""
# Program to check if a number is prime or not
num = 29

# To take input from the user
#num = int(input("Enter a number: "))

# define a flag variable
flag = False

# prime numbers are greater than 1
if num > 1:
    # check for factors
    for i in range(2, num):
        if (num % i) == 0:
            # if factor is found, set flag to True
            flag = True
            # break out of loop
            break

# check if flag is True
if flag:
    print(num, "is not a prime number")
else:
    print(num, "is a prime number")
"""
"""
for i in range(11):
    if i > 1:
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            print(i)
"""

""" 7.  i.  After getting a word from the user, your program should use while or for loop to print out each of the letters
            of the word. Just remember that strings in Python start with element 0!"""
"""
n = input("Enter the word: ")
lent = len(n)
for i in range(lent):
    print(n[i])
"""
"""     ii. Your program should then use another loop to print out each of the letters of the word in reverse order."""
"""
n = input("Enter word: ")
lent = len(n)
lent = lent - 1
while True:
    if lent == 0:
        print(n[lent])
        break
    else:
        print(n[lent])
        lent = lent - 1
"""

"""     iii.Make a new variable that is the original word in reverse and print that variable. You can do this very 
            easily in Python with a "string slice."""
"""
n = input("Enter word:")
lent = len(n)
lent = lent - 1
for i in range(lent, -1, -1):
    print(n[i])
"""

"""     iv. Ask the user for a letter to count. Use another loop to count how may times that letter appears 
            in the original word. Print out this count."""
"""
UserInput = input("Enter Word: ")
count = input("Enter alphabet want to count: ")
s = UserInput.count(count)
print(s)
"""

""" 8. Twisted Pig Latin. Prompt the user to enter a single word. Then form a new word by taking the first letter of
       the original word, moving it to the end, and adding "ay". Thus "school" becomes "choolsay"."""
"""
UserInput = input("Enter Single Word: ")
lent = len(UserInput)
lent = lent - 1
for i in UserInput:
    if i == 0:
        a = UserInput[i]
        b = UserInput[lent]
        UserInput[i] = b
        UserInput[lent] = a
        d = UserInput.extend("ay")
        print(d)
    else:
        continue
"""

""" 9.  Write a loop that prints out the index of every 'i' in 'Mississippi'. """
"""
n = "Mississippi"
lent = len(n)
s = n.count("i")
print(s, "i present in 'Mississippi'.\n\nIndexing are:-")
for a in range(lent):
    if n[a] == "i":
        print("Indexing -", a)
    else:
        continue
"""

""" 10. Write a program that prompts the user for two strings and checks if one of the strings is a prefix of the other.
        Print an appropriate message to inform the user which is the prefix or that neither is a prefix. For example,
        if the user input "evergreen" and "ever", the program would respond: "ever" is a prefix of "evergreen". But if
        the input was "evergreen" and "green", the program would respond that neither is a prefix of the other."""
"""
str = input("Enter Word: ")
pre = input("Enter prefix: ")
if str[: len(pre)] == pre:
    print(pre, "is a prefix of", str)
else:
    print(pre, "is not a prefix of", str)
"""

""" 11. Write another series which starts with 1, 1, 2. Every next number is defined as:
        (prev1 * prev2 + prev3). For nth ter, prev1 is the last number, prev2 is the second last number, ad prev3 is the
        third last number(N >= 3), i.e., series progress as:
        ......prev3, prev2, prev1, Nth term"""
"""
n = int(input("Enter No. of term:-"))
lst = [1]
for i in range(1, n - 1):
    lst.append(i)
print(lst)
lent = len(lst)
lent = lent - 1
prev1 = lst[lent - 3]
prev2 = lst[lent - 2]
prev3 = lst[lent - 1]
a = (prev1 * prev2) + prev3
print(a)
"""

""" 12. Write a program that prompts the user for a string s and a character c, and outputs the string produced form s
        by capitalizing each occurrence of the character c in s and making all other characters lowercase. For example, 
        if the user inputs "Mississippi" and "s", the program outputs "miSSiSSippi". """
"""
_input = "mississippi"
userinput = input("Enter Letter: ")
for i in _input:
    if userinput == i:
        a = userinput.upper()
        print(a, end="")
    else:
        b = i.lower()
        print(b, end="")
"""

""" 13. Write a program that prompts a user for their "password" and then determines if the password is valid or not. A
        password is said to be valid if it starts with digit and it has length 6 or more. If you program determines that
        user-entered password is not valid, it should print a message saying so. Otherwise, it should print a message 
        saying that is has accepted the user-entered password."""
"""
print("Enter Password must be 6 or more characters")
pin = input("Enter Password:")
pined = input("Enter User Password: ")
for i in pin[0]:
    if pin[0] == i.isnumeric():
        if pin == pined:
            print("User-entered pin is valid")
        else:
            print("User-entered pin is not valid")
    else:
        print("saying so")
"""
