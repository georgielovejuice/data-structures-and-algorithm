class BinaryTree:
    class Node:
        def __init__(self, data):
            self.data = data
            self.left = None
            self.right = None
        
        def __str__(self):
            return str(self.data)

    def __init__(self):
        self.root = None
    
    def insert(self, data):
        self.root = self._insert(self.root, data)
        return self.root
    
    def _insert(self, node, data):
        if node is None:
            return BinaryTree.Node(data)
        if data < node.data:
            node.left = self._insert(node.left, data)
        else:
            node.right = self._insert(node.right, data)
        return node

    def inorder(self):
        print("Inorder: ",end="")
        self._inorder(self.root)
        print()

    def _inorder(self, root):
        if root is not None:
            self._inorder(root.left)
            print(root.data, end=' ')
            self._inorder(root.right)

    def preorder(self):
        print("Preorder: ",end="")
        self._preorder(self.root)
        print()

    def _preorder(self, root):
        if root is not None:
            print(root.data, end=' ')
            self._preorder(root.left)
            self._preorder(root.right)

    def postorder(self):
        print("Postorder: ",end="")
        self._postorder(self.root)
        print()

    def _postorder(self, root):
        if root is not None:
            self._postorder(root.left)
            self._postorder(root.right)
            print(root.data, end=' ')

    def print_90_degree(self, root, level=0):
        if root is not None:
            self.print_90_degree(root.right, level + 1)
            print("     " * level, root.data)
            self.print_90_degree(root.left, level + 1)

tree = BinaryTree()
input = input("Enter number: ").split()
for i in input:
    root = tree.insert(int(i))
tree.inorder()
tree.preorder()
tree.postorder()
tree.print_90_degree(tree.root)