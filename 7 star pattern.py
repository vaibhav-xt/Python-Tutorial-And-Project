
# STAR PATTERN
"""
print
*
**
***
****

AND

****
***
**
*
"""

"""
print("How many Rows You want to print.")
a = int(input("Enter Number: "))
print("Type 0 and 1 :- ")
b = int(input())
new = bool(b)
if new == True:
    for i in range(1, a + 1):
        print("*" * i)
elif new == False:
    for i in range(a, 0, -1):
        print("*" * i)
"""
"""
print("How many Rows you want to print:")
    num = int(input("Enter Number: "))
    print("Type 0 and 1 :-")
    bin = int(input())
    try:
        if bin == 1:
            for i in range(1, num):
                print("*" * i)
        elif bin == 0:
            for i in range(num, 0, -1):
                print("*" * i)
        else:
            print("Invalid Input")
    except Exception as e:
        print("Invalid Input")
    print("Have A Nice Day")
"""
while True:
    print("      :--:STAR PATTERN:--:")
    print("""0. Print Star Pattern In Reverse Order\n1. Print Star Patten\n2. Exit""")
    choice = int(input("Enter You Choice:- "))
    if choice < 3:
        if choice == 2:
            print("Exit. *** Have a Nice Day ***")
            break
        elif bool(choice) == True:
            print("How many Rows you want to print:")
            num = int(input("Enter Number: "))
            for i in range(1, num + 1):
                print("*" * i)
        elif bool(choice) == False:
            print("How many Rows you want to print:")
            num = int(input("Enter Number: "))
            for i in range(num, 0, -1):
                print("*" * i)
    else:
        print("Entered Choice is Wrong.")

