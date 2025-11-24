""" 
* Queue using CLL code *
- Queue - A container in which the elements are placed one after another.
  So, the element which is placed earlier will be removed first.
- Working principle - First in First out (FIFO).
"""

class Node:
    def __init__(self, item=None, next=None):
        self.item = item
        self.next = next

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.len = 0

    def is_empty(self):
        return self.len == 0

    def enqueue(self, data):
        n = Node(data)
        if self.rear:
            self.rear.next = n
        else:
            self.front = n
        self.rear = n
        self.len += 1
    
    def dequeue(self):
        if self.front:
            data = self.front.item
            if self.front == self.rear:
                self.front = None
                self.rear = None
            else:
                self.front = self.front.next
            self.len -= 1
            return data
        raise IndexError("Queue is Empty!")
    
    def get_front(self):
        if self.rear:
            return self.front.item
        raise IndexError("Queue is Empty!")
    
    def get_rear(self):
        if self.rear:
            return self.rear.item
        raise IndexError("Queue is Empty!")
    
    def size(self):
        return self.len
    
if __name__ == '__main__':
    s = Queue()
    for i in range(20):
        s.enqueue(f"MSG_{i}")
    while s.size() > 0:
        print("Size: ", s.size())
        print("Front: ", s.get_front())
        print("Rear: ", s.get_rear())
        print("Dequeue: ", s.dequeue())
