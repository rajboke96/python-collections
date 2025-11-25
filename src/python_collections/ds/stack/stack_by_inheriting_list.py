""" 
* Stack by inheriting list *
- Stack - A container in which the elements are placed on top of each other.
- Working principle - Last in First out (LIFO).
"""

class Stack(list):
    top = 0
    def is_empty(self):
        return self == []

    def size(self):
        return len(self)
    
    def peek(self):
        return self[Stack.top]

    def push(self, data):
        super().insert(Stack.top, data)
    
    def pop(self):
        return super().pop(Stack.top)
    
    def insert(self, *args, **kwargs):
        raise AttributeError("No 'insert' attribute present in Stack class")
    
    def append(self, *args, **kwargs):
        raise AttributeError("No 'append' attribute present in Stack class")
    
    def remove(self, *args, **kwargs):
        raise AttributeError("No 'remove' attribute present in Stack class")

if __name__ == '__main__':
    s = Stack()
    for i in range(20):
        s.push(i)
    while s.size() > 0:
        print("Size: ", s.size())
        print("Peek: ", s.peek())
        print("Poped: ", s.pop())
