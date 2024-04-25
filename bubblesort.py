# wall is at the back
def bubblesort(arr):
    for wall in range(len(arr)):
        # implement 2 pointers j and j + 1
        for j in range(len(arr) - wall - 1):
            if (arr[j] > arr[j+1]):
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                
    return arr
                
print(bubblesort([-100, 5, 7, 4, 2]))