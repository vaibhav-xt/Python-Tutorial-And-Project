# Matrices

# addition of two matrices
"""
def matrix(m, n):
    o = []
    for i in range(m):
        row = []
        for j in range(n):
            inp = int(input(f"Enter O[{i}][{j}]"))
            row.append(inp)
        o.append(row)
    return o

def sum(A, B):
    output = []
    for i in range(len(A)):  # number of columns
        row = []
        for j in range(len(A[0])):  # number of rows
            row.append(A[i][j] + B[i][j])
        output.append(row)
    return output

m = int(input("Enter the value of m: "))
n = int(input("Enter the value of n: "))

print("Enter Matrix A")
A = matrix(m, n)
print(A)

print("Enter Matrix B")
B = matrix(m, n)

print(sum(A, B))
"""

# multiplication of two number

def matrix1(m, n):
    o = []
    for i in range(m):
        row = []
        for j in range(n):
            inp = int(input("Enter Values: "))
            row.append(inp)
        o.append(row)
    return o

def matrix2(y, x):
    o = []
    for i in range(x):
        row = []
        for j in range(y):
            inp = int(input("Enter Values: "))
            row.append(inp)
        o.append(row)
    return o

print("For A")
n = int(input("Enter Number of Columns: "))
m = int(input("Enter Number Of Rows: "))
print("\n")
A = matrix1(n, m)
print(f"Matrix A is {A}\n")

print("For B")
y = int(input("Enter Number of Columns: "))
x = int(input("Enter Number Of Rows: "))
print("\n")
B = matrix2(y, x)
print(f"Matrix B is {B}\n")

c = [[0 for x in range(x)] for y in range(n)]
if m == y:
    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                c[i][j] += A[i][k] * B[k][j]
    print(f"The Multiplication of {A} and {B} is {c}")
else:
    print(f"Multiplication of A and B is not possible.")

