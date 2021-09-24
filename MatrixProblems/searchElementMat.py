def searchElementMat1():
    row = int(input("enter the number of the rows"))
    col = int(input("enter the number of the column"))
    matrix = list()
    for i in range(row):
        a = list()
        for j in range(col):
            a.append(int(input("enter the data in the matrix")))
        matrix.append(a)
    print("the matrix element are ")
    for i in range(row):
        for j in range(col):
            print(matrix[i][j],end=" ")
        print()
    searchElement = int(input("enter the search element "))
    for i in range(row):
        for j in range(col):
            if (matrix[i][j]==searchElement):
                print("search Element is ","i:j",i,j,searchElement)
                break

searchElementMat1()
