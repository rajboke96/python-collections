""" 
* Queue using list *
- Queue - A container in which the elements are placed one after another.
  So, the element which is placed earlier will be removed first.
- Working principle - First in First out (FIFO).
"""

class Queue:
    front = 0
    rear = -1
    def __init__(self):
        self.items = []
    
    def enqueue(self, data):
        self.items.append(data)

    def dequeue(self):
        if self.items:
            return self.items.pop(Queue.front)
        raise IndexError("Queue is Empty!")
    
    def get_front(self):
        if self.items:
            return self.items[Queue.front]
        raise IndexError("Queue is Empty!")
    
    def get_rear(self):
        if self.items:
            return self.items[Queue.rear]
        raise IndexError("Queue is Empty!")
    
    def size(self):
        return len(self.items)
    
    def is_empty(self):
        return self.items == []
    
if __name__ == '__main__':
    s = Queue()
    for i in range(20):
        s.enqueue(i)
    while s.size() > 0:
        print("Size: ", s.size())
        print("Front: ", s.get_front())
        print("Rear: ", s.get_rear())
        print("Dequeue: ", s.dequeue())
