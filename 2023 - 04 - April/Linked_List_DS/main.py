class Node:
    def __init__(self, val=None):
        self.val = val
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = Node()

    def append(self, val):
        new_node = Node(val)
        curr_node = self.head
        while curr_node.next != None:
            curr_node = curr_node.next
        curr_node.next = new_node

linked_list = LinkedList()
linked_list.append(1)
linked_list.append(2)
linked_list.append(3)
print(linked_list)
