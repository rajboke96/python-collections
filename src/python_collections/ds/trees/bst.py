

class Node:
    def __init__(self, item=None, left=None, right=None):
        self.item = item
        self.left = left
        self.right = right

class BST:
    def __init__(self):
        self.root = None
        self.count = 0
    
    def insert(self, data):
        self.root = self.rinsert(self.root, data)
        self.count += 1
    
    def rinsert(self, root, data):
        if root is None:
            return Node(data)
        if data < root.item:
            root.left = self.rinsert(root.left, data)
        elif data > root.item:
            root.right = self.rinsert(root.right, data)
        return root
    
    def search(self, data):
        return self.rsearch(self.root, data)

    def rsearch(self, root, data):
        if root:
            if data == root.item:
                return root
            if data < root.item:
                return self.rsearch(root.left, data, root)
            elif data > root.item:
                return self.rsearch(root.right, data, root)

    def inorder(self):
        res = []
        self.rinorder(self.root, res)
        return res

    def rinorder(self, root, res):
        if root:
            self.rinorder(root.left, res)
            res.append(root.item)
            self.rinorder(root.right, res)

    def preorder(self):
        res = []
        self.rpreorder(self.root, res)
        return res

    def rpreorder(self, root, res):
        if root:
            res.append(root.item)
            self.rpreorder(root.left, res)
            self.rpreorder(root.right, res)

    def postorder(self):
        res = []
        self.rpostorder(self.root, res)
        return res

    def rpostorder(self, root, res):
        if root:
            self.rpostorder(root.left, res)
            self.rpostorder(root.right, res)
            res.append(root.item)

    def min(self):
        return self.rmin(self.root)

    def rmin(self, root):
        if root:
            if root.left:
                return self.rmin(root.left)
            else:
                return root.item
        
    def max(self):
        return self.rmax(self.root)
    
    def rmax(self, root):
        if root:
            if root.right:
                return self.rmax(root.right)
            else:
                return root.item
    
    def delete(self, data):
        self.root = self.rdelete(self.root, data)
        
    def rdelete(self, root, data):
        if root is None:
            return None
        if data < root.item:
            root.left = self.rdelete(root.left, data)
        elif data > root.item:
            root.right = self.rdelete(root.right, data)
        else:
            if not root.left:
                self.count -= 1
                return root.right
            elif not root.right:
                self.count -= 1
                return root.left
            else:
                root.item = self.rmax(root.left)
                root.left = self.rdelete(root.left, root.item)
        return root
    
    def size(self):
        return self.count

if __name__ == '__main__':
    bst = BST()
    l = [110, 9, 115, 8, 25, 112, 116, 20, 30, 113]
    for i in l:
        bst.insert(i)
    print("Size: ", bst.size())
    print("Inorder traverse: ", bst.inorder())
    bst.delete(9)
    bst.delete(112)
    bst.delete(1112)
    print("Size: ", bst.size())
    print("Inorder traverse: ", bst.inorder())
    print("Min Val: ", bst.min())
    print("Max Val: ", bst.max())
    # print("Preorder traverse: ", bst.preorder())
    # print("Postorder traverse: ", bst.postorder())
    # print("search: ", bst.search(0))