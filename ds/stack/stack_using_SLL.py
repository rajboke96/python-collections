""" 
* Stack using SLL *
- Stack - A container in which the elements are placed on top of each other.
- Working principle - Last in First out (LIFO).
"""

import sys
sys.path.append("../python-collections")

from linked_lists.sll import SLL

class Stack:
    def __init__(self):
        self.sll = SLL()
        self.len = 0

    def push(self, data):
        self.sll.insert_at_first(data)
        self.len += 1

    def pop(self):
        if not self.sll.is_empty():
            data = self.sll.start.item
            self.sll.delete_at_first()
            self.len -= 1
            return data
        else:
            raise Exception('Stack Empty!')
        
    def size(self):
        return self.len

    def peek(self):
        if self.sll.is_empty():
            raise Exception('Stack Empty!')
        return self.sll.start.item

    def is_empty(self):
        return self.sll.is_empty()
        
if __name__ == '__main__':
    s = Stack()
    for i in range(20):
        s.push(i)
    while s.size() > 0:
        print("Size: ", s.size())
        print("Peek: ", s.peek())
        print("Poped: ", s.pop())
