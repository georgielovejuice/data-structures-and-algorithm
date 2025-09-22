class Node:
    def __init__(self, data): 
        self.data = data  
        self.left = None  
        self.right = None 
        self.level = None 

    def __str__(self):
        return str(self.data) 

class BinarySearchTree:
    def __init__(self): 
        self.root = None

    def insert(self, val):
        self.root = self._insert(self.root, val)
        return self.root
    
    def _insert(self, node, val):
        if node is None:                
            return Node(val)
        if val < node.data:             
            node.left = self._insert(node.left, val)
        else:                           
            node.right = self._insert(node.right, val)
        return node
        
    def delete(self, node, data):
        if node is None:
            return None, False
        deleted = False
        if data < node.data: #หาNodeฝั่งซ้าย
            node.left, deleted= self.delete(node.left, data)
        elif data > node.data: #หาNodeฝั่งขวา
            node.right, deleted = self.delete(node.right, data)
        else: #เจอNodeที่จะลบ
            deleted = True
            if node.left is None and node.right is None: #No child #หรือเจอค่าที่จะลบเป็น root #Leaf node
                return None, True
            elif node.left is None: #One child
                return node.right, True
            elif node.right is None: 
                return node.left, True
            else: #Two children
                successor = self.findMin(node.right)
                node.data = successor.data
                node.right, _ = self.delete(node.right, successor.data)
        return node, deleted
    
    def findMin(self, node):
        while node.left is not None:
            node = node.left
        return node
    
def printTree90(node, level = 0):
    if node != None:
        printTree90(node.right, level + 1)
        print('     ' * level, node)
        printTree90(node.left, level + 1)


tree = BinarySearchTree()
data = input("Enter Input : ").split(",")
for e in data:
    cmd = e.split()
    if cmd[0] == "i":
        tree.insert(int(cmd[1]))
        print(f"insert {cmd[1]}")
        printTree90(tree.root)
    elif cmd[0] == "d":
        tree.root, deleted = tree.delete(tree.root, int(cmd[1]))
        if deleted:
            print(f"delete {cmd[1]}")
        else:
            print(f"delete {cmd[1]} \nError! Not Found DATA")
        printTree90(tree.root)

