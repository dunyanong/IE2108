def siftup(arr, i):
    temp = arr[i]
    
    while (i > 1 and temp > arr[i//2]):
        arr[i] = arr[i//2]
        i = i // 2
        
    arr[i] = temp