i = input("Input Value: ")
j = input("Input Value: ")
try:
    print(int(i) + int(j))    # Try Except are use to print the statement next if first is wrong.
except Exception as e:
    print(e)
print("This line is very important.")