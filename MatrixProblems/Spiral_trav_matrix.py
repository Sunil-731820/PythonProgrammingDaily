def Spiral_traversal():
    m = int(input("enter the number of row"))
    n = int(input("enter the number of the column"))
    matrix1 = []
    for i in range(m):
        list1 = list()
        for j in range(n):
            list1.append(int(input("enter the data in the list")))
        matrix1.append(list1)
    print("the element of the matrix is ")
    for i in range(m):
        for j in range(n):
            print(matrix1[i][j],end=" ")
        print()
    #displaying the traversal of the given matrix
    k = 0
    l = 0
    while(k<m and l <n):
        for i in range(l,n):
            print(matrix1[k][i],end=" ")
        k = k+1
Spiral_traversal()