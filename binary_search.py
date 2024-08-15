def binary_search(sorted_list, target):
    low = 0
    high = len(sorted_list) - 1

    while low <= high:
        mid = (high + low) // 2
        
        if sorted_list[mid] < target:
            low = mid + 1
        elif sorted_list[mid] > target:
            high = mid - 1
        else:
            print("Element found at index:", mid)
            return  # Exit the function after finding the element
    
    print("Oops... Element not found")

# Example usage
list1 = [2, 3, 23, 5, 32, 21]
list1.sort()  # Sorting the list
print("Your List is", list1)

k = int(input("Enter the element to be searched: "))
binary_search(list1, k)
