
# SUM OF THE DIGITS OF THE NUMBER

a = int(input("Enter the number you want sum of its:"))
s = 0
if a >= 0:
    r = a % 10
    s = s + r
    a = a // 10
    print(s)
