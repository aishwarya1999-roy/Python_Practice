"""class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
    def insert_at_beginnin(self, data):
        node  = Node(data, self.head)
        self.head = node

    def print(self):
        if self.head is None:
            print("Linked list is empty")
            return
        itr = self.head
        llstr = ''
        while itr :
            llstr += str(itr.data) + ' --> '
            itr = itr.next
        print(llstr)

if __name__ == '__main__':
    ll = LinkedList()
    ll.insert_at_beginnin(5)
    ll.insert_at_beginnin(10)
    ll.print()"""

from collections import deque
linked_list = deque()
linked_list.append(2)
linked_list.appendleft(1)
linked_list.pop()
print(linked_list)