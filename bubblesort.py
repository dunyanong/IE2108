def bubblesort(arr):
    for wall in range(len(arr)):
        # create two pointers
        for j in range(len(arr) -  wall - 1):
            if (arr[j] > arr[j+1]):
                arr[j], arr[j+1] = arr[j+1], arr[j]
                
    return arr

print(bubblesort([50, 10, 7, 4, 2]))