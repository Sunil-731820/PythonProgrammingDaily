def LowerTrimat():
    row = int(input("enter the number of the rows"))
    col = int(input("enter the number of the column"))
    matrix = list()
    for i in range(row):
        a = list()
        for j in range(col):
            a.append(int(input("enter the data in the array")))
        matrix.append(a)
    #displaying the matrix
    for i in range(row):
        for j in range(col):
            print(matrix[i][j],end=" ")
        print()
    print("\n")
    #displaying the lower triangular matrix
    for i in range(row):
        for j in range(col):
            if (i < j):
                print("0",end=" ")
            else:
                print(matrix[i][j],end=" ")
        print()
    print("displaying the upper triangular matrix ")
    #displaying the upper triangular matrix
    for i in range(row):
        for j in range(col):
            if (i>j):
                print("0",end=" ")
            else:
                print(matrix[i][j],end=" ")
        print()
    print("displaying the diagonal element is ")
    #displaying the diagonal element of the matrix
    for i in range(row):
        for j in range(col):
            if (i==j):
                print(matrix[i][j],end=" ")
        # print()
    print("the 2d matrix is ")
    for i in range(row):
        for j in range(col):
            print(matrix[i][j],end=" ")
        print()
    print("the alternate element is ")
    #displaying the alternate element in the 2d matrix
    for i in range(row):
        counter = 0
        for j in range(col):
            if j%2==0:
                # counter + =1
                pass

LowerTrimat()
