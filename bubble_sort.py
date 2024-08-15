def bubble_sort(list1):
    swap=0
    compare=0
    for i in range(0,len(list1)-1):  
        for j in range(len(list1)-i-1):  
            compare=compare+1
            if(list1[j]>list1[j+1]):  
                temp = list1[j]  
                list1[j] = list1[j+1]  
                list1[j+1] = temp
                swap=swap+1
    print("Swaps:",swap)
    print("Comparision:",compare) 

list1 = [8,7,6,5,3,2]
print("The unsorted list is: ", list1)
bubble_sort(list1)
print("The sorted list is: ",list1) 

