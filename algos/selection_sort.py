# Test Cases

# 1. l = [5, 4, 3, 2, 1]
# [5, 4, 3, 2, 1]
# [1, 4, 3, 2, 5]
# [1, 2, 3, 4, 5]
# [1, 2, 3, 4, 5]
# res = [1, 2, 3, 4, 5]

# 2. l = [20, 100, 50, 10, 80, 90, 70]
# [20, 100, 50, 10, 80, 90, 70]
# [10, 100, 50, 20, 80, 90, 70]
# [10, 20, 50, 100, 80, 90, 70]
# [10, 20, 50, 100, 80, 90, 70]
# [10, 20, 50, 70, 80, 90, 100]
# [10, 20, 50, 70, 80, 90, 100]
# res = [10, 20, 50, 70, 80, 90, 100]

class SelectionSort:
    def sort(l):
        print(f"Sorting with Selection sort algorithm")
        print(f"Input List - {l}")
        for i in range(len(l)-1):
            min = i
            for j in range(i+1, len(l)):
                if l[j] < l[min]:
                    min = j
            tmp = l[i]
            l[i] = l[min]
            l[min] = tmp
            # print(f"i{i} - {l}")
        print(f"After sorting, list - {l}")
        return l

if __name__ == '__main__':
    # l = [5, 4, 3, 2, 1]
    # l = [20, 100, 50, 10, 80, 90, 70]
    # l = [10, 20, 50, 70, 80, 90, 100]
    l = [20, 100, 50, 10, 80, 90, 70, 23, 23434, 2312, 444, 2]
    SelectionSort.sort(l)