""" Doubly Linked List """

class Node:
    def __init__(self, prev=None, item=None, next=None):
        self.prev = prev
        self.item = item
        self.next = next

class DLL:
    def __init__(self):
        self.start = None

    def __iter__(self):
        self.next_node = self.start
        return self

    def __next__(self):
        if(self.next_node):
            n = self.next_node
            self.next_node = self.next_node.next
            return n.item
        else:
            raise StopIteration 

    def is_empty(self):
        if self.start:
            return False
        return True
    
    def print_all(self):
        for i in self:
            print(i, end=' ')
        print()
    
    def search(self, data):
        current_node = self.start
        while (current_node and current_node.item != data):
            current_node = current_node.next
        if current_node:
            return current_node
    
    def insert_at_first(self, data):
        if(not self.start):
            n = Node(None, data, None)
            self.start = n
        else:
            n = Node(None, data, self.start)
            self.start.prev = n
            self.start = n

    def insert_at_last(self, data):
        if(not self.start):
            n = Node(None, data, None)
            self.start = n
        else:
            last_node = self.start
            while(last_node.next):
                last_node = last_node.next
            n = Node(last_node, data, last_node.next)
            last_node.next = n

    def insert_after(self, n, data):
        if n:
            temp = Node(n, data, n.next)
            if n.next:
                n.next.prev = temp
            n.next = temp

    def delete_at_first(self):
        if(self.start):
            self.start = self.start.next
            if(self.start): 
                self.start.prev = None

    def delete_at_last(self):
        if (self.start):
            last_node = self.start
            while(last_node.next):
                last_node = last_node.next
            if last_node.prev:
                last_node.prev.next = None
            else:
                self.start = None

    def delete_item(self, n):
        if n:
            if n.prev:
                n.prev.next = n.next
            if n.next:
                n.next.prev = n.prev
            elif not n.prev:
                self.start = None


if __name__ == '__main__':
    l1 = DLL()
    
    l1.insert_at_last(10)
    l1.insert_at_last(20)
    l1.insert_at_last(5)

    print ("Is list empty: ", l1.is_empty())

    search_val = 10
    print(f"Searching '{search_val}':", 'Found' if l1.search(search_val) else 'Not Found' )
    res = l1.search(search_val)
    # l1.insert_after(res, 200)
    
    l1.print_all()
    l1.delete_at_last()
    l1.print_all()
    l1.delete_at_last()
    l1.print_all()


