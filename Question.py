# 1. Write a program which will keep adding a stream of numbers inputted by the user. The adding stops as soon as
#    user presses q key on the keyboard.
"""
sum = 0
num_items = 0
num = 0
lst = []
while True:
    n = input("Enter the Prices if stop press q:- ")
    if n != "q":
        sum = sum + int(n)
        num_items = num_items + 1
        print("Actual Sum: ", sum, "\n")
    else:
        print("Total Sum is", sum, ". Thanks For Shopping With Us.\n")
        break
    num = num + 1
    lst.append(n)
print("Numbers Of Items Purchased: ", num)
lent = len(lst)
for i in range(lent):
    print(i + 1, ". ", lst[i])
"""
# 2. Factorial

def factorial(number):
    if number == 0 or number == 1:
        return 1
    else:
        return number * factorial(number - 1)

def  factorialTrailingZeroes(number):   # trailing zeroes means that number of zeroes in number
    fac = factorial(number)
    print(fac)
    count = 0
    while(fac % 10 == 0):
        count = count + 1
        fac = fac / 10
    return count
if __name__ == '__main__':
    # number = int(input("Enter a number: "))
    # fac = factorial(number)
    # print(f"The factorial is {fac}")
    print(factorialTrailingZeroes(20))


