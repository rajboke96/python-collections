
import sys
sys.path.append("/home/rajendra/projects/python_proj/DSA_PYTHON")

from stack.stack_using_SLL_concept import Stack

class Node:
    def __init__(self, item=None, left=None, right=None):
        self.item = item
        self.left = left
        self.right = right

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def post_traverse(self):
        if self.root:
            tmp = {
                'node': self.root,
                'isLeftComplete': False,
                'isrightComplete': False
            }
            s = Stack()
            while True:
                if not tmp['isLeftComplete']:
                    if tmp['node'].left:
                        s.push(tmp)
                        tmp['isLeftComplete'] = True
                        tmp = {
                            'node': tmp['node'].left,
                            'isLeftComplete': False,
                            'isrightComplete': False
                        }
                    else:
                        tmp['isLeftComplete'] = True
                elif not tmp['isrightComplete']:
                    if tmp['node'].right:
                        s.push(tmp)
                        tmp['isrightComplete'] = True
                        tmp = {
                            'node': tmp['node'].right,
                            'isLeftComplete': False,
                            'isrightComplete': False
                        }
                    else:
                        tmp['isrightComplete'] = True
                else:
                    print("Node Value: ", tmp['node'].item)
                    if s.is_empty():
                        break
                    else:
                        tmp = s.pop()

    def pre_traverse(self):
        if self.root:
            tmp = {
                'node': self.root, 'status': 'root'
            }
            s = Stack()
            while True:
                if tmp['status'] == 'root':
                    print("Node val: ", tmp)
                    if tmp['node'].left:
                        s.push(tmp)
                        tmp = {
                            tmp['node'].left
                        }
                elif tmp['status'] == 'left':
                    if tmp['node'].right:
                        s.push(tmp)
                        tmp = {
                            tmp['node'].right
                        }
                else:
                    if not s.is_empty:
                        tmp = s.pop()
                    else:
                        break

    def insert(self, data):
        n = Node(data)
        if not self.root:
            self.root = n
        else:
            tmp = self.root
            while True:
                if tmp.item < data:
                    if tmp.right:
                        tmp = tmp.right
                    else:
                        tmp.right = n
                        break
                elif tmp.item > data:
                    if tmp.left:
                        tmp = tmp.left
                    else:
                        tmp.left = n
                        break
                else:
                    break

bst = BinarySearchTree()
bst.insert(100)
bst.insert(50)
bst.insert(55)
bst.insert(60)
bst.insert(110)
bst.insert(12)
bst.insert(150)
bst.post_traverse()