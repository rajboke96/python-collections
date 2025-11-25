"""
* Priority Queue using list *
- Priority Queue - A container in which elements are placed one after another based on 
it's priority.
"""

class PriorityData:
    def __init__(self, p_no, item=None):
        self.p_no = p_no
        self.item = item

    def __str__(self):
        return "PriorityData(" + f"p_no = {self.p_no}, item = {self.item})"

class PriorityQueue:
    def __init__(self):
        self.items = []
    
    def is_empty(self):
        return len(self.items) == 0
    
    def get_size(self):
        return len(self.items)
    
    def get_priority_position(self, p_no):
        low = 0
        high = len(self.items) - 1
        while low <= high:
            mid = (low + high) // 2
            tmp = self.items[mid]
            if p_no >= tmp.p_no:
                low = mid + 1
            elif p_no < tmp.p_no:
                high = mid - 1
        if low > mid:
            index = low
        else:
            index = mid
        return index

    def push(self, p_no, data):
        pdata = PriorityData(p_no, data)
        if not self.items:
            self.items.append(pdata)
        else:
            index = self.get_priority_position(p_no)
            self.items.insert(index, pdata)

    def pop(self):
        if len(self.items) > 0:
            return self.items.pop(0).item
        raise IndexError("Priority Queue Underflow!")
    
    def print(self):
        for i in self.items:
            print((i.p_no, i.item), end='\n')
        print()

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