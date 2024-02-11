# Build a singly linked list
# Create a node with a data part and a next part
class Node:
    # constructor
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

# A Linked List class with a single head node
class LinkedList:
    def __init__(self):
        self.head = None

    # Insert a node to the linked list
    def insert(self, data):
        newNode = Node(data)
        if self.head:
            current = self.head
            while current.next:
                current = current.next
            current.next = newNode
        else:
            self.head = newNode

# Linked List with a single node
LL = LinkedList()  # create a linked list
LL.head = Node(10)  # head points to a node with data = 10
print(LL.head.data)  # 10 will be printed
LL.insert(20)  # Now LL has two nodes: 10 - 20
LL.insert(30)  # Now LL has three nodes: 10 – 20 - 30

current = LL.head  # current is the head pointer of LL
while current:  # if current is not None
    print(current.data, end=" – ")  # print current node
    current = current.next  # advance to the next node
