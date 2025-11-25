""" circular Linked List """

class Node:
    def __init__(self, item=None, next=None):
        self.item = item
        self.next = next


class CLLIterator:
    def __init__(self, last=None):
        self.last = last
        if self.last:
            self.current_node = self.last.next
        else:
            self.current_node = None

    def __next__(self):
        if self.current_node:
            data = self.current_node.item
            if self.current_node.next == self.last.next:
                self.current_node = None
            else:
                self.current_node = self.current_node.next
            return data
        else:
            raise StopIteration


class CLL:
    def __init__(self, last=None):
        self.last = last

    def __iter__(self):
        return CLLIterator(self.last)

    def is_empty(self):
        return self.last == None
    
    def print_all(self):
        if self.last:
            temp = self.last.next
            while True:
                print(temp.item, end=' ')
                if temp.next == self.last.next:
                    break
                temp = temp.next
            print()
    
    def insert_at_first(self, data):
        if self.last:
            n = Node(data, self.last.next)
            self.last.next = n
        else:
            n = Node(data)
            self.last = self.last.next = n

    def insert_at_last(self, data):
        if self.last:
            n = Node(data, self.last.next)
            self.last.next = n
            self.last = n
        else:
            n = Node(data)
            self.last = self.last.next = n

    def search(self, data):
        if self.last:
            temp = self.last
            while True:
                if temp.item == data:
                    return temp
                if temp.next == self.last:
                    break
                temp = temp.next

    def insert_after(self, n, data):
        if n:
            temp = Node(data, n.next)
            n.next = temp
            if n == self.last:
                self.last = temp

    def delete_first(self):
        if self.last:
            if self.last.next == self.last:
                self.last = None
            else:
                self.last.next = self.last.next.next

    def delete_last(self):
        if self.last:
            if self.last.next == self.last:
                self.last = None
            else:
                temp = self.last
                while temp.next != self.last:
                    temp = temp.next
                temp.next = self.last.next
                self.last = temp

    def delete_item(self, data):
        if self.last:
            temp = self.last.next
            while True:
                if temp.next.item == data:
                    if temp.next == temp.next.next:
                        self.last = None
                        break
                    if temp.next == self.last:
                        self.last = temp
                    temp.next = temp.next.next
                    break
                if temp.next == self.last.next:
                    break
                temp = temp.next
    
if __name__ == '__main__':
    l1 = CLL()
    l1.insert_at_first(50)
    l1.insert_at_first(100)
    l1.insert_after(l1.search(50), 1000)
    l1.print_all()
    l1.delete_item(1000)
    l1.delete_item(200)
    for i in l1:
        print(i, end=' ')
    print()
    print("List is empty: ", l1.is_empty())


