"""Circular Doubly Linked List"""

class Node:
    def __init__(self, prev, item, next):
        self.prev = prev
        self.item = item
        self.next = next

class CDLLIterator:
    def __init__(self, start=None):
        self.start = start
        self.current_node = start
    
    def __next__(self):
        if self.current_node:
            data = self.current_node.item
            self.current_node = self.current_node.next
            if self.current_node == self.start:
                self.current_node = None
            return data
        else:
            raise StopIteration

class CDLL:
    def __init__(self, start=None):
        self.start = start
        len = 0
        if self.start:
            temp = self.start
            while True:
                len += 1
                if (temp.next == self.start):
                    break
                temp = temp.next
        self.len = len

    def __iter__(self):
        return CDLLIterator(self.start)
    
    def __len__(self):
        return self.len

    def is_empty(self):
        return self.start == None
    
    def print_all(self):
        if self.start:
            temp = self.start
            while True:
                print(temp.item, end=' ')
                if temp.next == self.start:
                    break
                temp = temp.next
            print()

    def insert_at_first(self, data):
        if self.start:
            n = Node(self.start.prev, data, self.start)
            self.start.prev.next = n
            self.start.prev = n
            self.start = n
        else:
            n = Node(None, data, None)
            n.prev = n
            n.next = n
            self.start = n
        self.len += 1
    
    def insert_at_last(self, data):
        if self.start: 
            n = Node(self.start.prev, data, self.start)
            self.start.prev.next = n
            self.start.prev = n
        else:
            n = Node(None, data, None)
            n.prev = n
            n.next = n
            self.start = n
        self.len += 1

    def search(self, data):
        if self.start:
            temp = self.start
            while True:
                if temp.item == data:
                    return temp
                if temp.next == self.start:
                    break
                temp = temp.next
        return None
    
    def insert_after(self, temp, data):
        if temp:
            n = Node(temp, data, temp.next)
            temp.next.prev = n
            temp.next = n
            self.len += 1

    def delete_first(self):
        if self.start:
            if self.start.next == self.start:
                self.start = None
            else:
                self.start.next.prev = self.start.prev
                self.start.prev.next = self.start.next
                self.start = self.start.next
            self.len -= 1
        
    def delete_last(self):
        if self.start:
            if self.start.next == self.start:
                self.start = None
            else:
                self.start.prev.prev.next = self.start
                self.start.prev = self.start.prev.prev
            self.len -= 1

    def delete_item(self, data):
        if self.start:
            temp = self.start
            while True:
                if temp.item == data:
                    if temp == self.start:
                        self.delete_first()
                    elif temp == self.start.prev:
                        self.delete_last()
                    else:
                        temp.prev.next = temp.next
                        temp.next.prev = temp.prev
                    self.len -= 1
                if temp.next == self.start:
                    break
                temp = temp.next


if __name__ == '__main__':
    l1 =  CDLL()
    for i in range(0, 20):
        l1.insert_at_first(i)
    for j in range(len(l1)):
        l1.print_all()
        l1.delete_last()