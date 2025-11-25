""" 
* Stack using list *
- Stack - A container in which the elements are placed on top of each other.
- Working principle - Last in First out (LIFO).
"""

class Stack:
    top = 0
    def __init__(self):
        self.stk = list()

    def is_empty(self):
        return self.stk == []
    
    def size(self):
        return len(self.stk)
    
    def push(self, data):
        self.stk.insert(Stack.top, data)

    def pop(self):
        if self.stk:
            return self.stk.pop(Stack.top)
        else:
            raise Exception('Stack Empty!')

    def peek(self):
        if self.stk:
            return self.stk[Stack.top]
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