# LCM
a = int(input("Enter first Number: "))
b = int(input("Enter Second Number:"))
maxNum = max(a, b)

while True:
    if maxNum % a == 0 and maxNum % b == 0:
        break
    maxNum = maxNum + 1

print(f"The LCM of {a} and {b} is {maxNum}")

# HCF

m = int(input("Enter Number: "))
n = int(input("Enter Second Number: "))

if m < n:
    smaller = m
else:
    smaller = n
for i in range(1, smaller + 1):
    if m % i == 0 and n % i == 0:
        hcf = i

print(f"HCF of {m} and {n} is {hcf}.")
