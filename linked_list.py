class ListNode:
    def __init__(self, data):
        self.data = data
        self.next = None

def insert(start, node):
    if start is None or node.data <= start.data:
        node.next = start
        return node

    p_1 = start
    p_2 = start.next

    while p_2:
        if p_1.data <= node.data <= p_2.data:
            p_1.next = node
            node.next = p_2
            return start
            
        p_1 = p_2
        p_2 = p_2.next


    return start
