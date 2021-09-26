def matrix(columns, rows, matrix_name):
    for i in range(columns):
        row = []
        for j in range(rows):
            user_value = int(input("Enter the value: "))
            row.append(user_value)
        matrix_name.append(row)

def addmatrix(A, B):
    output = []
    for i in range(len(A)):
        row = []
        for j in range(len(A[0])):
            row.append(A[i][j] + B[i][j])
        output.append(row)
    return output


print("For Matrix A")
columns_A = int(input("Enter Number of Columns: "))
rows_A = int(input("Enter Number of Rows: "))
A = []
matrix(columns_A, rows_A, A)
print(f"A = {A}")

print("For Matrix B")
columns_B = int(input("Enter Number of Columns: "))
rows_B = int(input("Enter Number of Rows: "))
B = []
matrix(columns_B, rows_B, B)
print(f"B = {B}")


print("Adding result of two A and B matrices is")
print(f"C = {addmatrix(A, B)}")