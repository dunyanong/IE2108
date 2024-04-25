class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def find(src, x):
    current = src
    if current is None:
        return None
    
    if x == current.val:
        return current.val
    elif x < current.val:
        return find(current.left, x)
    else:
        return find(current.right, x)

        

root = TreeNode(5)
root.left = TreeNode(3)
root.right = TreeNode(7)
root.left.left = TreeNode(2)
root.left.right = TreeNode(4)
root.right.left = TreeNode(6)
root.right.right = TreeNode(8)

print(find(root, 2))