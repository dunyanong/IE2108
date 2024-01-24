def max_heapify(arr, heap_size, root_index):
    # Find the largest among the root, left child, and right child
    largest = root_index

    # Calculate the index of the left child of the current node.
    # The left child of a node at index 'root_index' is at '2 * root_index + 1'.
    left_child_index = 2 * root_index + 1

    # Calculate the index of the right child of the current node.
    # The right child of a node at index 'root_index' is at '2 * root_index + 2'.
    right_child_index = 2 * root_index + 2

    # Check if the left child is larger than the current largest
    if left_child_index < heap_size and arr[left_child_index] > arr[largest]:
        largest = left_child_index

    # Check if the right child is larger than the current largest
    if right_child_index < heap_size and arr[right_child_index] > arr[largest]:
        largest = right_child_index

    # If the largest element is not the root, swap them and recursively siftdown
    if largest != root_index:
        arr[root_index], arr[largest] = arr[largest], arr[root_index]
        max_heapify(arr, heap_size, largest)


arr = [4, 10, 3, 5, 1]
heap_size = len(arr)
root_index = 0

# Call max_heapify to siftdown the heap starting from the root
max_heapify(arr, heap_size, root_index)
print("Max heap after siftdown:", arr)