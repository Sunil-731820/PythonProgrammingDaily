def maximum_value():
    size = int(input("enter the size of the array"))
    arr = list()
    for i in range(size):
        data = int(input("enter the data "))
        arr.append(data)
    for j in range(size):
        print(arr[j],end=' ')
    max_value = arr[0]
    index =0 
    for k in range(1,size):
        if (arr[k]>max_value):
            max_value = arr[k]
            index+=1 
    print("\nthe maximum element is  ",max_value)
    print("the index of the ,maximum value is ",index)
    print("the index of the left index will be")
    print(index-1)
maximum_value()