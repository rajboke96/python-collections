class Deque:
    def __init__(self):
        self.items = []
    
    def is_empty(self):
        return len(self.items) == 0
    
    def insert_at_front(self, data):
        self.items.insert(0, data)

    def insert_at_rear(self, data):
        self.items.append(data)

    def delete_front(self):
        if self.items:
            return self.items.pop(0)
        raise IndexError("Deque Underflow")
    
    def delete_rear(self):
        if self.items:
            return self.items.pop(-1)
        raise IndexError("Deque Underflow")

    def get_front(self):
        if self.items:
            return self.items[0]
        raise IndexError("Deque Underflow")
    
    def get_rear(self):
        if self.items:
            return self.items[-1]
        raise IndexError("Deque Underflow")
    
    def size(self):
        return len(self.items)
    

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
