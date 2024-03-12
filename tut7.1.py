def swap(A, i, j):  # Function to swap elements at indices i and j in array A
    temp = A[i]
    A[i] = A[j]
    A[j] = temp

def partition(A, i, j):  # Function to partition the array A from indices i to j
    val = A[i]  # Choosing the first element as pivot
    h = i  # Initialize the pivot index
    for k in range(i + 1, j + 1):  # Loop through the elements from i+1 to j
        if A[k] < val:  # If the current element is less than pivot
            h = h + 1  # Increment the pivot index
            swap(A, h, k)  # Swap the current element with the element at pivot index
    swap(A, i, h)  # Swap the pivot element with the element at pivot index
    return h  # Return the pivot index after partitioning

def quicksort(A, p, r):  # Function to perform quicksort on array A from indices p to r
    if p < r:  # Base case: If p is less than r
        h = partition(A, p, r)  # Partition the array A
        quicksort(A, p, h - 1)  # Recursively sort the left partition
        quicksort(A, h + 1, r)  # Recursively sort the right partition

a = [10, 88, 36, 72, 26, 16, 42, 64, 12, 38]
print("before quicksort: ", a)
quicksort(a, 0, len(a) - 1)
print("after quicksort: ", a)












