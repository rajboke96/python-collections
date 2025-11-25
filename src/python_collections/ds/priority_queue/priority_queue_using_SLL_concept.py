"""
* Priority Queue using SLL concept *
- Priority Queue - A container in which elements are placed one after another based on 
it's priority.
"""

class Node:
    def __init__(self, item=None, next=None):
        self.item = item
        self.next = next

class PriorityData:
    def __init__(self, p_no, item=None):
        self.p_no = p_no
        self.item = item
    
    def __str__(self):
        return "PriorityData(" + f"p_no = {self.p_no}, item = {self.item})"

class PriorityQueue:
    def __init__(self):
        self.start = None
        self.count = 0

    def is_empty(self):
        return self.start == None
    
    def get_size(self):
        return self.count
    
    def push(self, p_no, data):
        pdata = PriorityData(p_no, data)
        if not self.start or self.start.item.p_no > p_no:
                n = Node(pdata, self.start)
                self.start = n
        else:
            tmp = self.start
            while tmp.next:
                if tmp.next.item.p_no > p_no:
                    n = Node(pdata, tmp.next)
                    tmp.next = n
                    return
                tmp = tmp.next
            n = Node(pdata)
            tmp.next = n
        self.count += 1
    
    def pop(self):
        if self.start:
            pdata = self.start.item
            self.start = self.start.next
            self.count -= 1
            return pdata
        raise IndexError("Priority Queue Underflow!")

    def print(self):
        tmp = self.start
        while tmp:
            print(tmp.item, end='\n')
            tmp = tmp.next
    

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