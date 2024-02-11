class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self, root_value):
        self.root = TreeNode(root_value)

# Creating the binary tree
binary_tree = BinaryTree(14)
node_6 = TreeNode(6)
node_18 = TreeNode(18)
node_3 = TreeNode(3)
node_7 = TreeNode(7)
node_15 = TreeNode(15)
node_19 = TreeNode(19)
node_17 = TreeNode(17)
node_16 = TreeNode(16)

# Constructing the tree structure
binary_tree.root.left = node_6
binary_tree.root.right = node_18
node_6.left = node_3
node_6.right = node_7
node_18.left = node_15
node_18.right = node_19
node_15.right = node_17

# Displaying the binary tree
def print_tree(node):
    if node is not None:
        print_tree(node.left)
        print(node.value)
        print_tree(node.right)

print_tree(binary_tree.root)

# Define the insertion function outside TreeNode class
def BSTinsert_recurs(root, temp):
    if temp.value <= root.value:
        if root.left is None:
            root.left = temp
        else:
            BSTinsert_recurs(root.left, temp)
    else:
        if root.right is None:
            root.right = temp
        else:
            BSTinsert_recurs(root.right, temp)

# Insert a new node
BSTinsert_recurs(binary_tree.root, node_16)

# Display the updated tree
print_tree(binary_tree.root)

def LeafCounter(T):
    if T == None: return 0

    return 1 + LeafCounter(T.left) + LeafCounter(T.right)


print(f"number of leaves: {LeafCounter(binary_tree.root)}")


def dfs_height(node):
    if not node:
        return 0
    
    left_height = dfs_height(node.left)
    right_height = dfs_height(node.right)
    
    return 1 + max(left_height, right_height)

print(dfs_height(binary_tree.root))

def jointTogether(Q, P):
    if len(P) == 0: 
        return
    
    Q.append(P.pop(0))    
    jointTogether(Q, P)


# Testing the function
Q = ['a', 'b', 'c', 'd']
P = ['e', 'f', 14]

jointTogether(Q, P)

print("Queue Q after appending P:", Q)
print("Queue P after operation:", P)