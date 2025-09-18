class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def __str__(self):
        return str(self.data)

class BST:
    def __init__(self):
        self.root = None

    def insert(self, data):
        self.root = self._insert(self.root, data)
        return self.root
    
    def _insert(self, node, data):
        if node is None:
            return Node(data)
        if data < node.data:
            node.left = self._insert(node.left, data)
        else:
            node.right = self._insert(node.right, data)
        return node
    
    def inorder(self, node):
        if node:
            self.inorder(node.left)
            print(node.data, end=' ')
            self.inorder(node.right)

    def preorder(self, node):
        if node:
            print(node.data, end=' ')
            self.preorder(node.left)
            self.preorder(node.right)

    def postorder(self, node):
        if node:
            self.postorder(node.left)
            self.postorder(node.right)
            print(node.data, end=' ')
T = BST()
input = input('Enter Input : ').split() #Example: 10 4 20 1 Inorder
inp = []
for data in input:
    if data.isdigit():
        inp.append(int(data))
    else:
        command = data
for i in inp:
    root = T.insert(i)
if command == 'Inorder':
    T.inorder(root)
elif command == 'Preorder':
    T.preorder(root)
elif command == 'Postorder':
    T.postorder(root)


