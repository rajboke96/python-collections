"""
* Stack by inheriting SLL *
- Stack - A container in which the elements are placed on top of each other.
- Working principle - Last in First out (LIFO).
"""

import sys
sys.path.append("/home/rajendra/projects/python_proj/DSA_PYTHON")

from sll import SLL

class Stack(SLL):
    def push(self, data):
        self.insert_at_first(data)
    
    def pop(self):
        if self.start:
            data = self.start.item
            self.delete_at_first()
            return data
        else:
            raise Exception('Stack Empty!')
    
    def size(self):
        return self.len
    
    def peek(self):
        if self.start:
            return self.start.item
        else:
            raise Exception('Stack Empty!')

if __name__ == '__main__':
    s = Stack()
    for i in range(20):
        s.push(i)
    while s.size() > 0:
        print("Size: ", s.size())
        print("Peek: ", s.peek())
        print("Poped: ", s.pop())
