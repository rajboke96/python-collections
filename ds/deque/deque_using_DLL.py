"""
Deque using DLL
"""

import sys
sys.path.append("../python-collections")

from dll import DLL

class Deque:
    def __init__(self):
        self.front = None
        self.rear = None
        self.item_count = 0
        self.items = DLL()

    def is_empty(self):
        return self.item_count == 0
    
    def insert_at_front(self, data):
        self.items.insert_at_first(data)
        if not self.front:
            self.front = self.items.start
            self.rear = self.items.start
        else:
            self.front = self.front.prev
        self.item_count += 1

    def insert_at_rear(self, data):
        if not self.front:
            self.items.insert_at_first(data)
            self.front = self.items.start
            self.rear = self.items.start
        else:
            self.items.insert_after(self.rear, data)
            self.rear = self.rear.next
        self.item_count += 1

    def delete_front(self):
        if self.front:
            data = self.front.item
            self.front = self.front.next
            self.items.delete_at_first()
            if not self.front:
                self.rear = None
            self.item_count -= 1
            return data
        raise IndexError("Deque Underflow")
    
    def delete_rear(self):
        if self.front:
            data = self.rear.item
            self.rear = self.rear.prev
            self.items.delete_item(self.rear)
            if not self.rear:
                self.front = None
            self.item_count -= 1
            return data
        raise IndexError("Deque Underflow")

    def get_front(self):
        if self.front:
            return self.front.item
        raise IndexError("Deque Underflow")
    
    def get_rear(self):
        if self.front:
            return self.rear.item
        raise IndexError("Deque Underflow")
    
    def size(self):
        return self.item_count
    

if __name__ == '__main__':
    d1 = Deque()
    d1.insert_at_front(20)
    d1.insert_at_front(10)
    d1.insert_at_rear(30)
    d1.insert_at_rear(40)
    d1.insert_at_rear(50)
    print("Total items in deque:", d1.size())
    print("Front item is:", d1.get_front())
    print("Rear item is:", d1.get_rear())
    d1.delete_front()
    print("Total items in deque:", d1.size())
    print("Front item is:", d1.get_front())
    print("Rear item is:", d1.get_rear())
    d1.delete_rear()
    print("Total items in deque:", d1.size())
    print("Front item is:", d1.get_front())
    print("Rear item is:", d1.get_rear())
