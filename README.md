# Python Data Structures & Algorithms 🚀

This repository contains my implementations of **Data Structures & Algorithms (DSA) in Python**, along with explanations, time complexities, and practice problems.
I’ve created this repo to strengthen my problem-solving skills and prepare for coding interviews.

---

## 📂 Contents

### 🔹 Data Structures & Algorithms

* Sorting Algorithms (Bubble, Selection & Insertion)
* Linked List(Singly, Doubly, Circular & Circular Doubly)
* Stack
* Queue(Queue, Deque & Priority Queue)
* Trees – (BST & AVL)
* Graph

---

## 🧠 Why This Repository?

* To build strong fundamentals in Python DSA
* To improve logical thinking
* To prepare for product-based company interviews
* To track my learning progress
* To contribute useful examples for others learning DSA

---

## 🗂️ Folder Structure

```
├── python-collections/
 ├── algos/
 ├── ds/
  ├── linked_list/
  ├── stack/
  ├── queue/
  ├── deque/
  ├── priority_queue/
  ├── trees/
  ├── graphs/
```

---

### ✅ **1. How to Install**

```bash
pip install git+https://github.com/rajboke96/python-collections
```

---

### 💡 **2. How to Import and Use**

## Usage Examples

### **1. Sorting Algorithms**
```python
from ds import BubbleSort, SelectionSort, InsertionSort

arr = [5, 2, 9, 1]
print("Original Array:", arr)
print("Bubble Sort:", BubbleSort.sort(arr))
print("Selection Sort:", SelectionSort.sort(arr))
print("Insertion Sort:", InsertionSort.sort(arr))
```
### 
### **2. Doubly Linked List**
```python
from ds.dll import DLL

l1 = DLL()
l1.insert_at_last(10)
l1.insert_at_last(20)
l1.insert_at_last(5)
print ("Is list empty: ", l1.is_empty())
search_val = 10
print(f"Searching '{search_val}':", 'Found' if l1.search(search_val) else 'Not Found' )
res = l1.search(search_val)
l1.insert_after(res, in 10)
l1.print_all()
l1.delete_at_last()
l1.print_all()
l1.delete_at_last()
l1.print_all()
```

## 🤝 Contributions

If you’d like to improve or add more algorithms, feel free to submit a pull request!

---

## ⭐ Support

If you find this useful, consider giving this repository a **star** ⭐
It motivates me to keep building and sharing!

---

## 📬 Connect with Me

If you’re also learning DSA or preparing for interviews, let’s connect!

* LinkedIn: *https://linkedin.com/in/rajendra-boke-947639199*
* GitHub: [https://github.com/rajboke96](https://github.com/rajboke96)

---
