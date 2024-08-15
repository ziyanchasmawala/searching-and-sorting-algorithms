def insertionSort(array):
    shift=0
    for i in range(1, len(array)):
        key = array[i]
        j = i - 1
        while j >= 0 and key < array[j]:
            shift+=1
            array[j + 1] = array[j]
            j = j - 1
        array[j + 1] = key
    print("No. of shifts:",shift)  

data = [90,56,45,34,12]
print("Original List is: ",data)
insertionSort(data)
print('Sorted Array is: ',data)

# def insertionSort(a):
#     shift=0
#     for i in range(1,len(a)):
        
#         temp=a[i]
#         j=i-1 
#         while(j>=0 and temp<a[j]):
#             shift=shift+1
#             a[j+1]=a[j]
#             j=j-1
#         a[j+1]=temp
        
#     print("No. of shifts:",shift)

# a=[9,8,7,6,5]
# print("Unsorted array:",a)
# insertionSort(a)
# print("Worst case sorted array:\n",a)
# print()

# b=[5,6,7,8,9]
# print("Unsorted array:",b)
# insertionSort(b)
# print("Best case sorted array:\n",b)
# print()

# c=[6,5,9,8,7]
# print("Unsorted array:",c)
# insertionSort(c)
# print("Average case sorted array:\n",c)
