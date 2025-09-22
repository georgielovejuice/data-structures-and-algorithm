class AVLTree:

    class AVLNode:
        def __init__(self, data, left = None, right = None):
            self.data = data
            self.left = None if left is None else left
            self.right = None if right is None else right
            self.height = self.setHeight()        

        def __str__(self):
            return str(self.data)

        def setHeight(self):
            self.height = 1 + max(self.getHeight(self.left), self.getHeight(self.right))
            return self.height            
        
        def getHeight(self, node):
            return -1 if node == None else node.height
           
        def balanceValue(self):
            return self.getHeight(self.right) - self.getHeight(self.left)


    def __init__(self, root = None):
        self.root = None if root is None else root

    def add(self, data):
        self.root = self._add(self.root, data)
        return self.root

    def _add(self, root, data):
        if root is None:
            return AVLTree.AVLNode(data)
        if data < root.data:
            root.left = self._add(root.left, data)
        else:
            root.right = self._add(root.right, data)

        root.setHeight()
        balance = root.balanceValue()

        if balance > 1:
            if root.right.balanceValue() < 0:
                root.right = AVLTree.rotateRightChild(root.right)
            return AVLTree.rotateLeftChild(root)

        if balance < -1:
            if root.left.balanceValue() > 0:
                root.left = AVLTree.rotateLeftChild(root.left)
            return AVLTree.rotateRightChild(root)
        
        return root
    
    def rotateLeftChild(root) : #RR Case คือหนักขวา
        newRoot = root.right
        root.right = newRoot.left
        newRoot.left = root
        root.setHeight()
        newRoot.setHeight()
        return newRoot

    def rotateRightChild(root) : #LL Case คือหนักซ้าย
        newRoot = root.left
        root.left = newRoot.right
        newRoot.right = root
        root.setHeight()
        newRoot.setHeight()
        return newRoot

    def postOrder(self):
        if self.root is not None:
            print("AVLTree post-order : ", end='')
            self._postOrder(self.root)
            print()
        else:
            print("AVLTree post-order : ")

    def _postOrder(self, root):
        if root is not None:
            self._postOrder(root.left)
            self._postOrder(root.right)
            print(root.data, end=' ')

    def printTree(self):
        if self.root is not None:
            self._printTree(self.root)
            print()
        else:
            print()

    def _printTree(self, node, level=0):
        if not node is None:
            self._printTree(node.right, level + 1)
            print('     ' * level, node.data)
            self._printTree(node.left, level + 1)

avl1 = AVLTree()
inp = input('Enter Input : ').split(',')
for i in inp:
    parts = i.strip().split()
    command = parts[0]
    if command == "AD":
        avl1.add(int(parts[1]))
    elif command == "PR":
        avl1.printTree()
    elif command == "PO":
        avl1.postOrder()