# -----------------------------------------------------------------------------------------------------------------------
# Question 2

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self, root_value):
        self.root = TreeNode(root_value)

root = TreeNode(5)
root.left = TreeNode(4)
root.right = TreeNode(7)
root.left.left = TreeNode(2)
root.left.right = TreeNode(1)
root.right.right = TreeNode(3)

def sumTree(root):
    if root is None: return 0
    
    leftSum = sumTree(root.left)
    rightSum = sumTree(root.right)
    
    return root.value + leftSum + rightSum

print(sumTree(root))

# -----------------------------------------------------------------------------------------------------------------------
# Q4) Siftdown recursion
def heapify(arr, n, i):
    largest = i  # Initialize largest as root
    left_child = 2 * i + 1  # left child index
    right_child = 2 * i + 2  # right child index

    # Compare left child with root
    if left_child < n and arr[largest] < arr[left_child]:
        largest = left_child

    # Compare right child with largest so far
    if right_child < n and arr[largest] < arr[right_child]:
        largest = right_child

    # Swap if needed
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # swap
        heapify(arr, n, largest)  # Heapify the affected subtree

def heapSort(arr):
    n = len(arr)

    # Build a max heap
    for i in range(n // 2, -1, -1):
        heapify(arr, n, i)
        
# Driver code to test above
arr = [3, 2, 8, 5, 1, 4]
heapSort(arr)
print('Sorted array is:', arr)

# -----------------------------------------------------------------------------------------------------------------------
# Q4) Siftdown iterative
def heapify(arr, n, i):
    largest = i  # Initialize largest as root
    while True:
        left_child = 2 * i + 1  # left child index
        right_child = 2 * i + 2  # right child index
        largest = i
        
        # Compare left child with root
        if left_child < n and arr[i] < arr[left_child]:
            largest = left_child

        # Compare right child with largest so far
        if right_child < n and arr[largest] < arr[right_child]:
            largest = right_child

        # Swap if needed
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]  # swap
            i = largest
        else:
            break

def heapSort(arr):
    n = len(arr)

    # Build a max heap
    for i in range(n // 2, -1, -1):
        heapify(arr, n, i)

    # Arranging the nodes based on value (left and right). left values < right
    for i in range(n - 1, 0, -1):
        print("arr[i], arr[0] = arr[0], arr[i]", arr)
        heapify(arr, i, 0)

# Driver code to test above
arr = [3, 2, 8, 5, 1, 4]
heapSort(arr)
print('Sorted array is:', arr)