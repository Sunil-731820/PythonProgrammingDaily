def MultiMatrix():
    global row,col
    row = int(input("enter the number of the rows"))
    col = int(input("enter the number of the column"))
    global matrix
    matrix1 = list()
    #taking the input from the the user for multiply
    for i in range(row):
        a = list()
        for j in range(col):
            a.append(int(input("enter the data in the matrix")))
        matrix1.append(a)
    #displaying the matrix for the simplicity
    for i in range(row):
        for j in range(col):
            print(matrix1[i][j],end=" ")
        print()
    global matrix2
    matrix2 = list()
    for i in range(row):
        b = list()
        for j in range(col):
            b.append(int(input("enter the data for the second matrix")))
        matrix2.append(b)
    #displaying the matrix 2 is
    for i in range(row):
        for j in range(col):
            print(matrix2[i][j],end=" ")
        print()

    #Adding the both the matrix are
    print("after the addition of the two matrix is ")
    addmatrix = list()
    for i in range(row):
        add1 = list()
        for j in range(col):
            add1.append(int(0))
        addmatrix.append(add1)
    for i in range(row):
        for j in range(col):
            addmatrix[i][j] = matrix1[i][j]+matrix2[i][j]
        print()
    #displaying the matrix after the addition
    for i in range(row):
        for j in range(col):
            print(addmatrix[i][j],end=" ")
        print()
    #storing the result as zero for the subtraction
    submatrix = list()
    for i in range(row):
        sub = list()
        for j in range(col):
            sub.append(int(0))
        submatrix.append(sub)
    #subtracting the two matrices are
    for i in range(row):
        for j in range(col):
            submatrix[i][j] = matrix1[i][j] - matrix2[i][j]
        print()
    print("the matrix after the subtraction is ")
    for i in range(row):
        for j in range(col):
            print(submatrix[i][j],end=" ")
        print()
    #storing the result as zero for the multiplication
    multMatrix = list()
    for i in range(row):
        mul = list()
        for j in range(col):
            mul.append(int(0))
        multMatrix.append(mul)
    print("after the multiplication of the matrix is ")
    print(len(matrix1))
    
    #displaying the matrix after the multiplication
    for i in range(row):
        for j in range(col):
            print(multMatrix[i][j],end=" ")
        print()
MultiMatrix()
