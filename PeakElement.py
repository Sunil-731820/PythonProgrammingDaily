def maximum_value():
    size = int(input("enter the size of the array"))
    arr = list()
    for i in range(size):
        data = int(input("enter the data "))
        arr.append(data)
    for j in range(size):
        print(arr[j],end=' ')
    max_value = arr[0]
    for k in range(1,size):
        if (arr[k]>max_value):
            max_value = arr[k]
    print("\nthe maximum element is  ",max_value)
maximum_value()