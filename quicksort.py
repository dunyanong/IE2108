# return index of the pivot
def partition(arr, low, high):
    # putting pivot at the back
    pivot = arr[high]
    i = low - 1
    
    for j in range(low, high):
        if (arr[j] < pivot):
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
            
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1
    

def quicksort(arr, low, high):
    if low < high:
        pivot_index = partition(arr, low, high)
    
        quicksort(arr, low, pivot_index - 1)
        quicksort(arr, pivot_index + 1, high)


# Example usage:
array_to_sort = [10, 7, 8, 9, 1, 5]
array_length = len(array_to_sort)
quicksort(array_to_sort, 0, array_length - 1)
print("Sorted array:", array_to_sort)
