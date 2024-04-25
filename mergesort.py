def merge_sort(arr):
    if len(arr) == 1:
        return arr
    
    mid = len(arr) // 2
    
    left = arr[:mid]
    right = arr[mid:]
    
    left = merge_sort(left)
    right = merge_sort(right)
    
    return merge(left, right)
    
def merge(x, y):
    # x = [1, 6, 4, 9, 7]
    # y = [3, 5, 6, 2, 1]
    x_pointer = 0
    y_pointer = 0
    res = []
    
    while (x_pointer < len(x) and y_pointer < len(y)):
        if x[x_pointer] <= y[y_pointer]:
            res.append(x[x_pointer])
            x_pointer += 1 
        else:
            res.append(y[y_pointer])
            y_pointer += 1
    
    res.extend(x[x_pointer:])
    res.extend(y[y_pointer:])
    
    return res

print(merge_sort([4, 3, 6, 2, 1, 8, 9]))