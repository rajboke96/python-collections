# Binary search


class Node:
    def __init__(self, item=None, left=None, right=None):
        self.item = item
        self.height = 0
        self.left = left
        self.right = right

class BST:
    def __init__(self):
        self.root = None
        self.count = 0

    def ll_rotation(self, o_root):
        n_root = o_root.left
        o_root.left = n_root.right
        n_root.right = o_root
        return n_root
    
    def rr_rotation(self, o_root):
        n_root = o_root.right
        o_root.right = n_root.left
        n_root.left = o_root
        return n_root
    
    def lr_rotation(self, o_root):
        # n_root = o_root.left.right
        # n_root.left = o_root.left
        # n_root.right = o_root
        # o_root.left.right = n_root.left
        # o_root.left = n_root.right
        # return n_root
        pass

    def rl_rotation(self, o_root):
        tmp = o_root.right.left
        o_root.right.left = tmp.right
        tmp.right = o_root.right

        o_root.right = tmp.left
        tmp.left = o_root
        return tmp
    
    def get_root_height(self, root):
        if not root:
            return 0
        left_subtree_height, right_subtree_height = -1, -1
        if root.left:
            left_subtree_height = root.left.height
        if root.right:
            right_subtree_height = root.right.height
        if left_subtree_height > right_subtree_height:
            return left_subtree_height + 1
        else:
            return right_subtree_height + 1
        
    def get_root_bf(self, root):
        if not root:
            return 0
        left_subtree_height, right_subtree_height = -1, -1
        if root.left:
            left_subtree_height = root.left.height
        if root.right:
            right_subtree_height = root.right.height
        return (left_subtree_height + 1) - (right_subtree_height + 1)

    def update_height(self, root, rotation_type):
        if rotation_type in ['ll', 'rr', 'lr', 'rl']:
            if rotation_type == 'll':
                root.right.height = self.get_root_height(root.right)
                root.height = self.get_root_height(root)
            if rotation_type == 'rr':
                root.left.height = self.get_root_height(root.left)
                root.height = self.get_root_height(root)
            if rotation_type == 'lr':
                root.right.height = self.get_root_height(root.right)
                root.height = self.get_root_height(root)
            if rotation_type == 'rl':
                print("Root --- ", root.item)
                root.right.height = self.get_root_height(root.right)
                root.left.height = self.get_root_height(root.right)
                root.height = self.get_root_height(root)
        else:
            raise TypeError("Invalid Rotation Type")
        
    def root_balance(self, root):
        a_balance_factor = self.get_root_bf(root)
        if a_balance_factor < -1 or a_balance_factor > 1 :
            print("Node -", root.item, "unbalanced", "with Balance Factor: ", a_balance_factor)
            self.print_balance_factor()
            print()
            # unbalanced after insertion.
            if a_balance_factor < -1:
                b_balance_factor = self.get_root_bf(root.right)
                if b_balance_factor == -1:
                    # rr rotation
                    n_root = self.rr_rotation(root)
                    self.update_height(n_root, 'rr')
                else:
                    # rl rotation
                    n_root = self.rl_rotation(root)
                    self.update_height(n_root, 'rl')
            else:
                b_balance_factor = self.get_root_bf(root.left)
                if b_balance_factor == 1:
                    # ll rotation
                    n_root = self.ll_rotation(root)
                    self.update_height(n_root, 'll')
                else:
                    # lr rotation
                    n_root = self.lr_rotation(root)
                    self.update_height(n_root, 'lr')
            return n_root
        else:
            return root

    def insert(self, data):
        self.root = self.rinsert(self.root, data)
        self.count += 1
        print("Inserted: ", data)
        self.print_balance_factor()
        print()
    
    def rinsert(self, root, data):
        if root is None:
            return Node(data)
        if data < root.item:
            root.left = self.rinsert(root.left, data)
        elif data > root.item:
            root.right = self.rinsert(root.right, data)
        root.height = self.get_root_height(root)
        return self.root_balance(root)      

    def print_balance_factor(self):
        self.rprint_balance_factor(self.root)

    def rprint_balance_factor(self, root):
        if root:
            self.rprint_balance_factor(root.left)
            print("Item:", root.item, "Balance Factor:", self.get_root_bf(root))
            self.rprint_balance_factor(root.right)
    
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
            res.append(root)
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
        print("Deleted: ", data)
        self.print_balance_factor()
        print()
        
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
        root.height = self.get_root_height(root)
        return self.root_balance(root)
    
    def size(self):
        return self.count

if __name__ == '__main__':
    bst = BST()
    l = [110, 9, 115, 8, 25, 112, 116, 20, 30, 113]
    # l = [i for i in range(1, 10)]
    for i in l:
        bst.insert(i)
    bst.delete(20)
    bst.delete(30)
    bst.delete(25)
    bst.delete(8)
    # bst.print_balance_factor()
    # print("Size: ", bst.size())
    # for root in bst.inorder():
    #     print("Item:", root.item, ", Height:", root.height, 
    #                   ", Balance Factor: ", bst.get_root_bf(root))
    # bst.delete(9)
    # bst.delete(112)
    # bst.delete(1112)
    # print("Size: ", bst.size())
    # for n in bst.inorder():
    #     print(n.item, n.height)
    # print("Min Val: ", bst.min())
    # print("Max Val: ", bst.max())
    # print("Preorder traverse: ", bst.preorder())
    # print("Postorder traverse: ", bst.postorder())
    # print("search: ", bst.search(0))