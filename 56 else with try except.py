f1 = open("mylogs.txt")

try:
    f = open("currency date.txt")

except Exception as e:
    print(e)

else:
    print("Else function will print if exception is not run.")

finally:  # finally is used that it will must to print.
    print("Run this any way")
    # f.close()
    f1.close()

print("Important Stuff")