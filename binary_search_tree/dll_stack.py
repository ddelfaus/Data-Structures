# import sys
# sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList

class Stack:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        self.storage = DoublyLinkedList()

    def push(self, value):
        #adding to the top of the stack
        self.storage.add_to_head(value)
        self.size += 1
    def pop(self):
        #removing top of stack
        if self.size > 0:
            val = self.storage.remove_from_head()
            self.size -= 1
            return val
        else:
            return None


    def len(self):
        return self.size
