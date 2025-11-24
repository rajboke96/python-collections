""" 
* Stack using SLL code *
- Stack - A container in which the elements are placed on top of each other.
- Working principle - Last in First out (LIFO).
"""

class Node:
    def __init__(self, item=None, next=None):
        self.item = item
        self.next = next
        
class Stack:
    def __init__(self):
        self.top = None
        self.len = 0

    def push(self, data):
        if self.top:
            n = Node(data, self.top)
        else:
            n = Node(data)
        self.top = n
        self.len += 1
    
    def pop(self):
        if self.top:
            data = self.top.item
            self.top = self.top.next
            self.len -= 1
            return data
        raise IndexError("Stack is Empty!")
    
    def peek(self):
        if self.top:
            return self.top.item
        raise IndexError("Stack is Empty!")
    
    def size(self):
        return self.len

    def is_empty(self):
        return self.top == None
    
if __name__ == '__main__':
    s = Stack()
    for i in range(20):
        s.push(i)
    while s.size() > 0:
        print("Size: ", s.size())
        print("Peek: ", s.peek())
        print("Poped: ", s.pop())
