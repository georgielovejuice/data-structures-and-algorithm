class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.data)

def build_expr_tree(postfix: str):
    ops = set("+-*/")
    stack = []
    for ch in postfix: #Example: ab+cde+**
        if ch == ' ':
            continue
        if ch in ops:
            r = stack.pop()
            l = stack.pop()
            n = Node(ch)
            n.left, n.right = l, r
            stack.append(n)
        else:
            stack.append(Node(ch))
    return stack[-1] if stack else None


def printTree90(node, level=0):
    if node is not None:
        printTree90(node.right, level + 1)
        print('     ' * level, node)   
        printTree90(node.left, level + 1)

def to_infix(node): #Example: ((a+b)*(c*(d+e)))
    if node is None:
        return ""
    if node.left is None and node.right is None:
        return str(node.data)
    return "(" + to_infix(node.left) + str(node.data) + to_infix(node.right) + ")"

def to_prefix(node): #Example: *+ab*c+de
    if node is None:
        return ""
    return str(node.data) + to_prefix(node.left) + to_prefix(node.right)


postfix = input("Enter Postfix : ")
root = build_expr_tree(postfix)

print("Tree :")
printTree90(root)
print("--------------------------------------------------")
print("Infix : " + to_infix(root))
print("Prefix : " + to_prefix(root))