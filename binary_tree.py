class Binary_Tree_Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, data):
        if data == self.data:
            return
        if data < self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left = Binary_Tree_Node(data)
        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = Binary_Tree_Node(data)

    def in_order_traversal(self):
        array = []
        if self.left:
            array += self.left.in_order_traversal()
        array.append(self.data)
        if self.right:
            array += self.right.in_order_traversal()
        return array

    def search(self, val):
        if self.data == val:
            return True
        if val < self.data:
            if self.left:
                return self.left.search(val)
        else:
            if self.right:
                return self.right.search(val)
        return False




root = Binary_Tree_Node(15)
root.add_child(7)
root.add_child(19)
root.add_child(3)
root.add_child(9)
root.add_child(2)
root.add_child(5)
root.add_child(17)
root.add_child(21)
print(root.search(5))
print(root.in_order_traversal())
