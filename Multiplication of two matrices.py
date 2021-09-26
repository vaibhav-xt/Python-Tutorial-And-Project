# Multiplication Two Matrices

def matrice(m, n):
    output = []
    for i in range(m):
        row = []
        for j in range(n):
            inp = int(input("Enter The Value: "))
            row.append(inp)
        output.append(row)
    return output

def multiple(A, B):
    C = [[0 for i in range(row_B)] for j in range(column_A)]
    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                C[i][j] += A[i][k] * B[k][j]
    return C

print("For Matrix A:")
column_A = int(input("Enter Number of Column: "))
row_A = int(input("Enter Number of Row: "))
A = matrice(column_A, row_A)
print(f"A = {A}")

print("For Matrix B: ")
column_B = int(input("Enter Number of Column: "))
row_B = int(input("Enter Number of Row: "))
B = matrice(column_B, row_B)
print(f"B = {B}")

if row_A == column_B:
    print(f"Result of Multiplication of A and B is {multiple(A, B)}")
else:
    print(f"row_A of A and Column of B is not equal. Hence Multiple of Two Matrices is not possible.")
