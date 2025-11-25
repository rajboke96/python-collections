""" 
* Queue using CLL *
- Queue - A container in which the elements are placed one after another.
  So, the element which is placed earlier will be removed first.
- Working principle - First in First out (FIFO).
"""



from python_collections.ds.linked_lists.sll import SLL

class Queue:
    def __init__(self):
        self.items = SLL()
        self.front = None
        self.rear = None
        self.len = 0

    def enqueue(self, data):
        if self.rear:
            self.items.insert_after(self.rear, data)
            self.rear = self.rear.next
        else:
            self.items.insert_at_first(data)
            self.front = self.items.start
            self.rear = self.items.start
        self.len += 1
    
    def dequeue(self):
        if self.items.is_empty():
            raise IndexError("Queue is Empty!")
        data = self.front.item
        if self.front == self.rear:
            self.rear = None
        self.items.delete_at_first()
        self.front = self.front.next
        self.len -= 1
        return data
    
    def get_front(self):
        if self.items.is_empty():
            raise IndexError("Queue is Empty!")
        data = self.front.item
        return data
    
    def get_rear(self):
        if self.items.is_empty():
            raise IndexError("Queue is Empty!")
        data = self.rear.item
        return data
    
    def size(self):
        return self.len
    
    def is_empty(self):
        return self.items.is_empty()

if __name__ == '__main__':
    s = Queue()
    for i in range(20):
        s.enqueue(i)
    while s.size() > 0:
        print("Size: ", s.size())
        print("Front: ", s.get_front())
        print("Rear: ", s.get_rear())
        print("Dequeue: ", s.dequeue())
