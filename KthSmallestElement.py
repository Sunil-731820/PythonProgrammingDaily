def KthSmallestelement():
    size = int(input("enter the size of the array"))
    arr = list()
    for i in range(size):
        data = int(input("enter the data first"))
        arr.append(data)
    for j in range(size):
        print(arr[j],end=" ")
    KthSmallest = int(input("enter the kthsmallest element to be find"))
    #applying the sorting algorithms to arrange the given data in sequences
    #in ascending order
    for k in range(size):
        for l in range(size):
            if (arr[k]>arr[l]):
                temp = arr[k]
                arr[k] = arr[l]
                arr[l] = temp
    revese1 = arr[::-1]
    print("after sorting the given data the array is ")
    for m in range(size):
        print(arr[m],end=" ")
    print("\n")
    for n in range(len(revese1)):
        print(revese1[n],end=" ")
    
    print("the KthSmallestElement in the array will be",revese1[KthSmallest-1])
KthSmallestelement()
    
