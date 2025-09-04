class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next
    
    def __str__(self):
        return str(self.data)


def create_list(l=[]):
    values_list = l.split(',') 
    head = None
    tail = None
    for value in values_list:
        new_node = Node(int(value))
        if head is None:
            head = new_node
        else:
            tail.next = new_node
        tail = new_node
    return head


def print_list(head):
    """Print all nodes in the list EIEI. ตัวอย่าง: Node 1 -> Node 2 -> Node 3"""
    current = head
    while current:
        print(current, end=' ')
        current = current.next
    print()


def merge_ordered_lists(p, q):
    """Merge two sorted linked lists into one sorted list. BRUH"""
    dummy = Node(0) 
    current = dummy
    
    while p and q:
        if p.data < q.data:
            current.next = p
            p = p.next
        else:
            current.next = q
            q = q.next
        current = current.next

    current.next = p if p else q
    return dummy.next


L1, L2 = input("Enter 2 Lists : ").split()
LL1 = create_list(L1)
LL2 = create_list(L2)
print('LL1 : ', end='')
print_list(LL1)
print('LL2 : ', end='')
print_list(LL2)
merged = merge_ordered_lists(LL1, LL2)
print('Merge Result : ', end='')
print_list(merged)

