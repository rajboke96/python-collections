""" Singly Linked List """

class Node:
    def __init__(self, data=None, next=None):
        self.item = data
        self.next = next

class SLLIterator:
    def __init__(self, start=None):
        self.current_node = start
    
    def __next__(self):
        if self.current_node:
            data = self.current_node.item
            self.current_node = self.current_node.next
            return data
        else:
            raise StopIteration

class SLL:
    def __init__(self, start=None):
        self.start = start
    
    def __iter__(self):
        return SLLIterator(self.start)
        
    def is_empty(self):
        return self.start == None
    
    def print_all(self):
        if self.start:
            current_node = self.start
            while (current_node):
                print(current_node.item, end=' ')
                current_node = current_node.next
            print()

    def insert_at_first(self, data):
        new_node = Node(data)
        new_node.next = self.start
        self.start = new_node


    def insert_at_last(self, data):
        new_node = Node(data)
        if (not self.start):
            self.start = new_node
        else:
            last_node = self.start
            while (last_node.next):
                last_node = last_node.next
            last_node.next = new_node


    def search(self, data):
        if self.start:
            temp = self.start
            while temp:
                if temp.item == data:
                    return temp
                temp = temp.next

    def insert_after(self, temp, data):
        if temp:
            n = Node(data, temp.next)
            temp.next = n

    def delete_at_first(self):
        if self.start:
            self.start = self.start.next
    
    def delete_item(self, data):
        if(self.start.item == data):
            self.delete_at_first()
        else:
            current_node = self.start
            while(current_node.next):
                if(current_node.next.item == data):
                    current_node.next = current_node.next.next
                    break
                current_node = current_node.next


if __name__ == '__main__':
    l1 = SLL()
    l1.insert_at_last(10)
    l1.insert_at_last(20)
    l1.insert_at_last(20)
    l1.insert_at_last(30)
    # l1.delete_item(20)
    l1.insert_after(l1.search(200), 1000)
    l1.print_all()
    # for i in l1:
    #     print(i, end=' ')
    # print()
