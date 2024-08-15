def bucketSort(array):
    bucket = []

    for i in range(len(array)):#create empty buckets
        bucket.append([])

    for j in array:#place elements in respective buckets
        index_b = int(10 * j)
        bucket[index_b].append(j)
        
    for i in range(len(array)):#sorting internally in buckets
        bucket[i] = sorted(bucket[i])

    k = 0
    for i in range(len(array)):
        for j in range(len(bucket[i])):
            array[k] = bucket[i][j]
            k += 1
    return array

array = [0.88,0.76,0.65,0.63,0.61,0.56,0.45,0.37,0.34,0.23,0.14]
print("Original array is: ",array)
bucketSort(array)
print("Sorted Array is",array)