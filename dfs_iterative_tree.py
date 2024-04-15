class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def dfs_iterative(root):
    res = []
    stack = [root]
    
    while stack:
        current = stack.pop()
        res.append(current.val)
        if current.right:
            stack.append(current.right)
        if current.left:
            stack.append(current.left)
            
    return res
        

# Example usage:
# Constructing a simple binary tree
#        1
#       / \
#      2   3
#     / \
#    4   5

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

print(dfs_iterative(root))