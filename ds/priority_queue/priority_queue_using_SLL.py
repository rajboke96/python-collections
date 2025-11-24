"""
Priority Queue using SLL
"""

import sys
sys.path.append("../python-collections")

from ds.linked_lists.sll import SLL

class PriorityData:
    def __init__(self, p_no, item=None):
        self.p_no = p_no
        self.item = item
    
    def __str__(self):
        return "PriorityData(" + f"p_no = {self.p_no}, item = {self.item})"

class PriorityQueue:
    def __init__(self):
        self.items = SLL()
        self.count = 0

    def is_empty(self):
        return self.count == 0

    def get_size(self):
        return self.count

    def push(self, p_no, data):
        pdata = PriorityData(p_no, data)
        if self.count == 0 or self.items.start.item.p_no > p_no:
            self.items.insert_at_first(pdata)
        else:
            tmp = self.items.start
            while tmp.next:
                if tmp.next.item.p_no > p_no:
                    self.items.insert_after(tmp, pdata)
                    return
                tmp = tmp.next
            else:
                self.items.insert_after(tmp, pdata)
        self.count += 1

    def pop(self):
        if self.count == 0:
            raise IndexError("Priority Queue Underflow!")
        pdata = self.items.start.item
        self.items.delete_at_first()
        self.count -= 1
        return pdata

    def print(self):
        for pdata in self.items:
            print(pdata, end="\n")


if __name__ == "__main__":
    pq = PriorityQueue()
    try:
        print("Poped:", pq.pop())
    except IndexError as e:
        print("Pop Failed:", e)
    pq.push(1, 10)
    pq.push(1, 20)
    pq.push(5, 20)
    pq.push(1, 30)
    pq.push(2, 20)
    pq.push(3, 30)
    pq.print()
    print("Size:", pq.get_size())
    print("Poped:", pq.pop())
    print("Size:", pq.get_size())
    pq.print()