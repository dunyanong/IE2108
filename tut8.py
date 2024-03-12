def binary_search(arr, left_index, right_index, target):
    mid = (left_index + right_index) // 2
    if (arr[mid] == target): return mid
    if (left_index > right_index): return "no value has been found"
    
    if (target < arr[mid]):
        return binary_search(arr, left_index, mid - 1, target)        
    else:
        return binary_search(arr, mid + 1, right_index, target)
            
    
test_arr = [1, 3, 5, 6, 7, 8, 9, 10, 11, 12]
print(binary_search(test_arr, 0, len(test_arr) - 1, 10))
