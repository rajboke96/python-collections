"""
* Deque by DLL Concept *
- Deque - TODO
"""

class Node:
    def __init__(self, prev=None, item=None, next=None):
        self.prev = prev
        self.item = item
        self.next = next

class Deque:
    def __init__(self):
        self.front = None
        self.rear = None
        self.item_count = 0

    def is_empty(self):
        return self.item_count == 0

    def insert_at_front(self, data):
        n = Node(None, data, self.front)
        if self.front:
            self.front.prev = n
        else:
            self.rear = n
        self.front = n
        self.item_count += 1
    
    def insert_at_rear(self, data):
        n = Node(self.rear, data, None)
        if self.front:
            self.rear.next = n
        else:
            self.front = n
        self.rear = n
        self.item_count += 1

    def delete_front(self):
        if self.front:
            front_data = self.front.item
            if self.front.next:
                self.front.next.prev = None
            else:
                self.rear = None
            self.front = self.front.next
            self.item_count -= 1
            return front_data
        raise IndexError("Deque Underflow")

    def delete_rear(self):
        if self.front:
            rear_data = self.rear.item
            if self.rear.prev:
                self.rear.prev.next = None
            else:
                self.front = None
            self.rear = self.rear.prev
            self.item_count -= 1
            return rear_data
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
