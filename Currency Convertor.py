with open("currency date.txt") as f:
    a = f.readlines()

currencyDict = {}
for line in a:
    parsed = line.split("\t")
    currencyDict[parsed[0]] = parsed[1]

amount = int(input("Enter Amount: "))
print("Enter the name of currency you want to convert this amount to? Available Option:\n")
[print(item) for item in currencyDict.keys()]
currency = input("Please enter one of these values")
print(f"{amount} INR is equal to {amount * float(currencyDict[currency])} {currency}.")
f.close()
