def search_element(list1, n):
    for x in range(len(list1)):
        if list1[x] == n:
            print("Element found at index:", x)
            return  # Exit the function after finding the element
    print("Element not found!")  # This only runs if the loop completes without finding the element

# Example usage
list1 = [23, 43, 12, 3, 56, 33]
n = int(input("Enter the number to be searched: "))
search_element(list1, n)
