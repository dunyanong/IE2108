def swap(A, i, j):
    # swap positions i and j of an array A
    temp = A[i]
    A[i] = A[j]
    A[j] = temp

def siftdown(A, i):
    n = len(A) - 1  # heap size 1..n
    largest = i
    left = 2 * i  # test for a left child
    if left <= n and A[left] > A[i]:
        largest = left
    right = 2 * i + 1  # test for a right child
    # if right child has a larger value, update largest
    if right <= n and A[right] > A[largest]:
        largest = right
    if largest != i:  # need to swap
        swap(A, i, largest)
        siftdown(A, largest)  # recursive call!!

a = [0, 16, 23, 31, 20, 4]  # a[0] is never used
print("array a: ", a[1:])
size = len(a) - 1
for i in range(int(size/2), 0, -1):
    siftdown(a, i)
    
print("siftdown: ", a[1:])
swap(a, 1, size)

print("shift to end: ", a[1:])
b = a[0:size]

print("array b: ", b[1:])
size = len(b) - 1
for i in range(int(size/2), 0, -1):
    siftdown(b, i)
print("siftdown: ", b[1:])