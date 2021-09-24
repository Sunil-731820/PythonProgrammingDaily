def ScalarMatrix():
    row = int(input("enter the number of the rows"))
    col = int(input("enter the number of the column"))
    matrix = list()
    for i in range(row):
        a = list()
        for j in range(col):
            a.append(int(input("enter the data for the array")))
        matrix.append(a)
    for i in range(row):
        for j in range(col):
            print(matrix[i][j],end=" ")
        print()
    scalar1 = int(input("enter the data for the scalar matrix"))
    for i in range(row):
        for j in range(col):
            matrix[i][j] = matrix[i][j]*scalar1
    print("after the multiplication of the scalar matrix is")
    for i in range(row):
        for j in range(col):
            print(matrix[i][j],end=" ")
        print()
ScalarMatrix()