def quicksort(arr, low, high):
    if low < high:
        pivot_index = partition(arr, low, high)
        
        quicksort(arr, low, pivot_index - 1)
        quicksort(arr, pivot_index + 1, high)
        
def partition (arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[j], arr[i] = arr[i], arr[j]
    
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    
    return i + 1 # return pivot index


# Example usage:
array_to_sort = [10, 7, 8, 9, 1, 5]
quicksort(array_to_sort, 0, len(array_to_sort) - 1)
print("Sorted array:", array_to_sort)