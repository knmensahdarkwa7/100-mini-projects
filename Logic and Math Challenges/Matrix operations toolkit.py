# Matrix operation based on user input

# Prompt the user to enter two comma-separated lists of integers
mat1 = list(map(int, input('Enter mat1 (comma-separated): ').split(',')))
mat2 = list(map(int, input('Enter mat2 (comma-separated): ').split(',')))
op = input('Which operator (+, -, or . for dot product): ').strip()

# Ensure both matrices have the same length
if len(mat1) != len(mat2):
    print("Error: Matrices must be of equal length.")
    exit()

result_matrix = []

# Define matrix addition
def add():
    for i in range(len(mat1)):
        result_matrix.append(mat1[i] + mat2[i])
    print(f"Result: [{', '.join(map(str, result_matrix))}]")

# Define matrix subtraction
def sub():
    for i in range(len(mat1)):
        result_matrix.append(mat1[i] - mat2[i])
    print(f"Result: [{', '.join(map(str, result_matrix))}]")

# Define element-wise dot product
def dot_product():
    for i in range(len(mat1)):
        result_matrix.append(mat1[i] * mat2[i])
    print(f"Result: [{', '.join(map(str, result_matrix))}]")

# Execute selected operation
if op == '+':
    add()
elif op == '-':
    sub()
elif op == '.':
    dot_product()
else:
    print("Unsupported operator. Use +, -, or . for dot product.")