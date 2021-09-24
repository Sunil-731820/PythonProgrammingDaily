def MaxRowWith():
    row = int(input("enter the number of the rows"))
    col = int(input("enter the number of the column"))
    matrix = []
    #taking the input matrix from the array
    for i in range(row):
        a = []
        for j in range(col):
            a.append(int(input("enter the data for the matrix")))
        matrix.append(a)
    #printing the element of the matrix
    for i in range(row):
        for j in range(col):
            print(matrix[i][j],end=" ")
        print("\n")
    global list1
    list1 = list()
    count1 = 0
    for i in range(row):
        for j in range(col):
            if matrix[i][j]==int(1):
                count1+=1
        list1.append(count1)
        count1 = 0
    print("the list of the all counter having the values 1 is ")
    print(list1)

def maxRow():
    max1 = list1[0]
    for i in range(len(list1)):
        if list1[i]>max1:
            max1 = list1[i]
            # break
    print("the maximum row will be",max1)
MaxRowWith()
maxRow()