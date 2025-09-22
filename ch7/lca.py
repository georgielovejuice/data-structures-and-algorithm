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
    
    def lca(self, node, n1, n2):
        if node is None:
            return None
        if node.data > n1 and node.data > n2: #Both n1 and n2 are in left subtree becuase node.data is greater than both
            return self.lca(node.left, n1, n2)
        if node.data < n1 and node.data < n2: #Both n1 and n2 are in right subtree becuase node.data is less than both
            return self.lca(node.right, n1, n2)
        return node

T = BST()
inp = [int(i) for i in input('Enter Input : ').split()]
for i in inp:
    root = T.insert(i)
n1, n2 = [int(i) for i in input('Enter Input 2 : ').split()]
ans = T.lca(root, n1, n2)
print(ans).

