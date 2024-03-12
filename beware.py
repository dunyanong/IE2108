def insert_into_priority_queue(array, key):
    # Append the key at the end of the array
    array.append(key)
    index = len(array) - 1
    
    # Percolate up to maintain the heap property
    while index > 0:
        parent_index = (index - 1) // 2
        if array[parent_index] <= key:
            break
        array[index] = array[parent_index]
        index = parent_index
    array[index] = key

# Example usage:
priority_queue = [2, 4, 7, 9, 10]
insert_into_priority_queue(priority_queue, 5)
print("Priority queue after insertion:", priority_queue)