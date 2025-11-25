""" 
* Queue by inheriting CLL *
- Queue - A container in which the elements are placed one after another.
  So, the element which is placed earlier will be removed first.
- Working principle - First in First out (FIFO).
"""



from python_collections.ds.linked_lists.sll import SLL

class Queue(SLL):
    def __init__(self):
        super().__init__()
        self.front = None
        self.rear = None
        self.len = 0

    def enqueue(self, data):
        if self.front:
            self.insert_after(self.rear, data)
            self.rear = self.rear.next
        else:
            self.insert_at_first(data)
            self.front = self.start
            self.rear = self.start
        self.len += 1

    def dequeue(self):
        if self.front:
            data = self.front.item
            if self.front == self.rear:
                self.rear = None
            self.front = self.front.next
            self.delete_at_first()
            self.len -= 1
            return data
        raise IndexError("Queue is Empty!")
    
    def get_front(self):
        if self.front:
            return self.front.item
        raise IndexError("Queue is Empty!")

    def get_rear(self):
        if self.rear:
            return self.rear.item
        raise IndexError("Queue is Empty!")

    def size(self):
        return self.len
    
    def is_empty(self):
        return self.is_empty()
    
if __name__ == '__main__':
    s = Queue()
    for i in range(20):
        s.enqueue(i)
    while s.size() > 0:
        print("Size: ", s.size())
        print("Front: ", s.get_front())
        print("Rear: ", s.get_rear())
        print("Dequeue: ", s.dequeue())
