mat1 = list(map(int, input('Enter mat1 (comma-separated): ').split(',')))
mat2 = list(map(int, input('Enter mat2 (comma-separated): ').split(',')))
op = input('Which operator (+ or -): ')
result_matrix = []

def add():
    for i in range(len(mat1)):
        result_matrix.append(mat1[i] + mat2[i])
    print("[" + ', '.join(str(x) for x in result_matrix) + "]")

def sub():
    for i in range(len(mat1)):
        result_matrix.append(mat1[i] - mat2[i])
    print("[" + ', '.join(str(x) for x in result_matrix) + "]")
def dot_product():
    for i in range(len(mat1)):
        result_matrix.append(mat1[i] * mat2[i])
    print("[" + ', '.join(str(x) for x in result_matrix) + "]")

if op == '+':
    add()
elif op == '-':
    sub()
elif op == '.':
    dot_product()
else:
    print("Unsupported operator.")