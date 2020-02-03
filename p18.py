a,b = [int(i) for i in input("Enter size of 1st matrix(m x n):").strip().split()]
c,d = [int(i) for i in input("Enter size of 2nd matrix(m x n):").strip().split()]
if b != c:
    print("Multiplication Not Possible!!")
else:
    print("enter values for matrix 1:")
    matrix1 = [[float(i) for i in input().strip().split()] for x in range(a)]
    print("enter values for matrix 2:")
    matrix2 = [[float(i) for i in input().strip().split()] for x in range(c)]
    matrix3 = [[sum(a * b for a, b in zip(row, col)) for col in zip(*matrix2)] for row in matrix1]
    print('ans:',matrix3)
