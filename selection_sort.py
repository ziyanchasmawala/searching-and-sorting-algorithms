def selectionSort(array):
    swap=0
    compare=0
    for i in range(len(array)):
        ind=i
        for j in range(i+1,len(array)):
            compare=compare+1
            if (array[j]<array[ind]):
                swap=swap+1
                ind=j
        (array[i],array[ind])=(array[ind],array[i])
        
    print("Swaps:",swap)
    print("Comparision:",compare)
        
a=[99,64,55,39,34,11]
print("Unsorted array is: ",a)
selectionSort(a)
print("Sorted array is : ",a)
print()

