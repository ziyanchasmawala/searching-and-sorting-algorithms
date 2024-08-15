def mergeSort(array):
    global compare
    compare=0
    if len(array) > 1:

        r = len(array)//2
        L = array[:r]
        M = array[r:]

        mergeSort(L)
        mergeSort(M)

        i = j = k = 0

        while i < len(L) and j < len(M):
            if L[i] < M[j]:
                array[k] = L[i]
                i += 1
            else:
                array[k] = M[j]
                j += 1
            k += 1
            compare=compare+1

        while i < len(L):
            array[k] = L[i]
            i += 1
            k += 1

        while j < len(M):
            array[k] = M[j]
            j += 1
            k += 1

# def printList(array):
#     for i in range(len(array)):
#         print(array[i], end=" ")
#     print()

array = [84,65,45,33,25,12]
print("Unsorted array is: ",array)
mergeSort(array)
print("Sorted array is: ",array)
print("No. of comparisions:",compare)



# def mergeSort(a):
#     global compare
#     compare=0
#     if (len(a)>1):
#         mid=len(a)//2
#         L=a[:mid]
#         R=a[mid:]
#         mergeSort(L)
#         mergeSort(R)
#         i=j=k=0
#         while i<len(L) and j<len(R):
#             if L[i]<=R[j]:
#                 a[k]=L[i]
#                 i+=1
#             else:
#                 a[k]=R[j]
#                 j+=1
#             k+=1
#             compare=compare+1       
#         while i<len(L):
#             a[k]=L[i]
#             i+=1
#             k+=1           
#         while j<len(R):
#             a[k]=R[j]
#             j+=1
#             k+=1    
# a=[5,4,3,2,1]
# print("Unsorted array:",a)
# mergeSort(a)
# print("Worst case sorted array:",a)
# print("No. of comparisions:",compare)
# print()
# b=[1,2,3,4,5]
# print("Unsorted array:",b)
# mergeSort(b)
# print("Best case sorted array:\n",b)
# print("No. of comparisions:",compare)
# print()
# c=[4,2,5,3,1]
# print("Unsorted array:",c)
# mergeSort(c)
# print("Average case sorted array:\n",c)
# print("No. of comparisions:",compare)

