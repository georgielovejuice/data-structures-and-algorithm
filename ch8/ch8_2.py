class Node: 
    def __init__(self, data): 
        self.data = data
        self.left = None
        self.right = None
        self.height = 1
    
    def __str__(self):
        return str(self.data)

class AVL_Tree:
    def __init__(self, root = None):
        self.root = None if root is None else root
    
    def getHeight(self, node):
        if not node:
            return 0
        return node.height

    def getBalance(self, node):
        if not node:
            return 0
        return self.getHeight(node.right) - self.getHeight(node.left)
    
    def insert(self, node, key):
        self.root = self._insert(node, key)
        return self.root

    def _insert(self, node, key):
        if not node:
            return Node(key)
        elif key < node.data:
            node.left = self._insert(node.left, key)
        else:
            node.right = self._insert(node.right, key)

        node.height = 1 + max(self.getHeight(node.left), self.getHeight(node.right))
        balance = self.getBalance(node)

        if balance > 1 or balance < -1:
            print("Not Balance, Rebalance!")
            if balance > 1:
                if key > node.right.data:
                    return self.rotateLeftChild(node)
                else:
                    node.right = self.rotateRightChild(node.right)
                    return self.rotateLeftChild(node)

            if balance < -1:
                if key < node.left.data:
                    return self.rotateRightChild(node)
                else:
                    node.left = self.rotateLeftChild(node.left)
                    return self.rotateRightChild(node)
        return node

    def rotateLeftChild(self, root) : #RR Case คือหนักขวา
        newRoot = root.right
        root.right = newRoot.left
        newRoot.left = root
        root.height = 1 + max(self.getHeight(root.left), self.getHeight(root.right))
        newRoot.height = 1 + max(self.getHeight(newRoot.left), self.getHeight(newRoot.right))
        return newRoot
    
    def rotateRightChild(self, root): #LL Case คือหนักซ้าย
        newRoot = root.left
        root.left = newRoot.right
        newRoot.right = root
        root.height = 1 + max(self.getHeight(root.left), self.getHeight(root.right))
        newRoot.height = 1 + max(self.getHeight(newRoot.left), self.getHeight(newRoot.right))
        return newRoot

def printTree90(node, level = 0):
    if node != None:
        printTree90(node.right, level + 1)
        print('     ' * level, node)
        printTree90(node.left, level + 1)
  
myTree = AVL_Tree() 
root = None

data = input("Enter Input : ").split()
for e in data:
    print("insert :",e)
    root = myTree.insert(root, (int(e)))
    printTree90(root)
    print("===============")