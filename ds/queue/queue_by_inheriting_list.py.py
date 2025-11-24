""" 
* Queue by inheriting List *
- Queue - A container in which the elements are placed one after another.
  So, the element which is placed earlier will be removed first.
- Working principle - First in First out (FIFO).
"""

class Queue(list):
    front = 0
    rear = -1
    def enqueue(self, data):
        self.append(data)
    
    def dequeue(self):
        if self:
            return self.pop(Queue.front)
        raise IndexError("Queue is Empty!")

    def get_front(self):
        if self:
            return self[Queue.front]
        raise IndexError("Queue is Empty!")
    
    def get_rear(self):
        if self:
            return self[Queue.rear]
        raise IndexError("Queue is Empty!")
    
    def size(self):
        return len(self)
    
    def is_empty(self):
        return self == []
    
if __name__ == '__main__':
    s = Queue()
    for i in range(20):
        s.enqueue(i)
    while s.size() > 0:
        print("Size: ", s.size())
        print("Front: ", s.get_front())
        print("Rear: ", s.get_rear())
        print("Dequeue: ", s.dequeue())