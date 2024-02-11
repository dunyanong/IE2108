class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):
        if self.data:  # If the node is not empty
            if data < self.data:  # Go to the left subtree
                if self.left is None:  # If no left subtree exists
                    self.left = Node(data)  # Place the node here
                else:
                    self.left.insert(data)  # Recursively call insert() on the left subtree
            elif data > self.data:  # Go to the right subtree
                if self.right is None:  # If no right subtree exists
                    self.right = Node(data)
                else:
                    self.right.insert(data)  # Recursively call insert() on the right subtree
        else:
            self.data = data  # If the node is empty, set the data

    def PrintTree(self):
        if self.left: 
            self.left.PrintTree()        
        if self.right:
            self.right.PrintTree()
        print(self.data)            


# Use the insert method to add nodes
root = Node(12)
root.insert(6)
root.insert(14)
root.insert(3)
root.insert(10)
root.PrintTree()