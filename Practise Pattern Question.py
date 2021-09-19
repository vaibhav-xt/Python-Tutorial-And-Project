# 1 PYRAMID PRINTING
"""
for i in range(0, 6):
    for j in range(0, i):
        print("*", end="")
    print("*")
"""

# 2 NUMBER PYRAMID
"""
n = int(input("Enter a number of n: "))
for i in range(n):
    print("" * (n - i - 1), end="")
    for j in range(i + 1):
        print(i + 1, "", end="")
    print()
"""
# alternate method
"""
for i in range(1, 6):
    for j in range(1, i):
        print(j, end="")
    print(i)
"""

# 3 ALPHABETICAL PYRAMID
"""
n = int(input("Enter a number of rows: "))
for i in range(n):
    print((chr(65 + i) + "") * (i + 1))
"""

# 4 DIAMOND PRINTING
"""
n = int(input("Enter a number of n: "))
for i in range(n):
    print(" " * (n - i - 1), end="")
    for j in range(i + 1):
        print("* ", end="")
    print()
for i in range(n - 1):
    print(" " * (i + 1), end="")
    for j in range(n - i - 1):
         print("* ", end="")
    print()
"""

# 5 Hollow Printing Pattern
"""
n = int(input("Enter a number of n: "))
for i in range(n):
    print(" " * (n - i - 1) + "* ", end="")
if i >= 1:
    print("" * (2 * i - 1) + "* ", end="")
    print()
"""

# 6 Rectangle Pattern
"""
         * * * * *
         *       *
         *       *
         *       *
         * * * * *
"""
# Can't make for any number
"""
n = 5
print("# " * n)
for i in range(1, n - 1):
    print("# ", "  " * 2, "#")
print("# " * n)
"""

# 7 Z-Shape Pattern
"""
n = 5
print("# " * n)
for i in range(0, n + 1):
    print(" " * i, "# ")
print("# " * n)
"""

# 8 Z- reverse Pattern
"""
n = 5
print("# " * n)
for i in range(n + 1, -1, -1):
    print(" " * i, "# ")
print("# " * n)
"""

# 9 Z - star pattern
"""
n = int(input("Enter Number: "))
print("* " * n)
for i in range(n - 1, 0, -1):
    print("  " * (i - 1), "*")
print("* " * n)
"""

# 10. star pattern
"""
n = int(input("Enter No. of Rows: "))
for i in range(n, 0, -1):
    print("* " * i)
"""

# 11. square pattern
"""
n = int(input("Enter No. of Rows: "))
for i in range(n):
    print(" " * n, "* " * n)
for i in range(n):
    print("* " * n)
"""

# 12.
n = 12
for i in range(0, n):
    print(" " * (n - i), "* " * i)
for i in range(n, 0, -1):
    print(" " * (n - i), "* " * i)



