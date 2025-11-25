# Test Cases

# 1. l = [5, 4, 3, 2, 1]
# [5, 4, 3, 2, 1]
# [4, 3, 2, 1, 5]
# [3, 2, 1, 4, 5]
# [2, 1, 3, 4, 5]
# [1, 2, 3, 4, 5]
# res = [1, 2, 3, 4, 5]

# 2. l = [20, 100, 50, 10, 80, 90, 70]
# [20, 100, 50, 10, 80, 90, 70]
# [20, 50, 10, 80, 90, 70, 100]
# [20, 10, 50, 80, 70, 90, 100]
# [10, 20, 50, 70, 80, 90, 100]
# [10, 20, 50, 70, 80, 90, 100]
# [10, 20, 50, 70, 80, 90, 100]
# [10, 20, 50, 70, 80, 90, 100]
# res = [10, 20, 50, 70, 80, 90, 100]

class BubbleSort:
    def sort(l):
        print(f"Sorting with Bubble sort algorithm")
        print(f"Input List - {l}")
        shift_count = 0
        for i in range(len(l)-1):
            is_sorted = True
            for j in range(len(l)-i-1):
                if l[j] > l[j+1]:
                    # print(f"Shifting {l[j]} <-> {l[j+1]}")
                    is_sorted = False
                    tmp = l[j]
                    l[j] = l[j+1]
                    l[j+1] = tmp
                    shift_count += 1
            if is_sorted:
                break
            # print(f"i{i} - {l}")
        print(f"shift_count - {shift_count}")
        print(f"After sorting, list - {l}")
        return l

if __name__ == '__main__':
    # l = [5, 4, 3, 2, 1]
    # l = [20, 100, 50, 10, 80, 90, 70]
    # l = [10, 20, 50, 70, 80, 90, 100]
    l = [20, 100, 50, 10, 80, 90, 70, 23, 23434, 2312, 444, 2]
    BubbleSort.sort(l)
