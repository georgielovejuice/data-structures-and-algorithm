class BinaryTree:

    class Node:
        def __init__(self, data = None):
            self.data = data
            self.left = None
            self.right = None
            self.height = 0

        def __str__(self):
            return str(self.data)
        
        def getheight(self, node):
            if node is None:
                return -1
            return node.height
    
        def setheight(self):
            self.height = 1 + max(self.getheight(self.left), self.getheight(self.right))
            return self.height

        def balanceValue(self):
            return self.getheight(self.right) - self.getheight(self.left)

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

        node.setheight()
        balance = node.balanceValue()

        if balance > 1:
            if node.right.balanceValue() < 0: #RL Case
                print("Right Left Rotation")
                node.right = self.rotateRight(node.right)
                return self.rotateLeft(node)
            print("Right Right Rotation")
            return self.rotateLeft(node)

        if balance < -1:
            if node.left.balanceValue() > 0: #LR Case
                print("Left Right Rotation")
                node.left = self.rotateLeft(node.left)
                return self.rotateRight(node)
            print("Left Left Rotation")
            return self.rotateRight(node)
        return node

    def rotateLeft(self, root): #หนักขวา
        new_root = root.right
        root.right = new_root.left
        new_root.left = root
        root.setheight()
        new_root.setheight()
        return new_root

    def rotateRight(self, root): #หนักซ้าย
        new_root = root.left
        root.left = new_root.right
        new_root.right = root
        root.setheight()
        new_root.setheight()
        return new_root

    def printTree90(self):
        if self.root is not None:
            print("Tree structure:")
            self._printTree90(self.root)

    def _printTree90(self, node, level=0):
        if node is not None:
            self._printTree90(node.right, level + 1)
            print("     " * level, node.data)
            self._printTree90(node.left, level + 1)


tree = BinaryTree()
inp = [int(i) for i in input('Enter Input : ').split()]
for i in inp:
    root = tree.insert(int(i))
    tree.printTree90()
    print("==============================")
