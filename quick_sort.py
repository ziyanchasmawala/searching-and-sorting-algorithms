def quickSort(array):
    if len(array)<=1:
        return array    
    pivot=array[-1]
    left,right=[],[]
    for i in range(len(array)-1):
        if (array[i]<pivot):
            left.append(array[i])
        else:
            right.append(array[i])
    return quickSort(left)+[pivot]+quickSort(right)

data=[65,54,34,33,25,12]
print("Unsorted array is: ",data)
print("Sorted array is: ",quickSort(data))

