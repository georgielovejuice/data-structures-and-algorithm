def display_rods(A, B, C):
    """Display rods as vertical stacks"""
    print("|  |  |")
    for i in range(n-1, -1, -1):  # print from top to bottom อันบนสุดคือจะมีแต่ rod
        left = str(A[i]) if i < len(A) else "|"
        middle = str(B[i]) if i < len(B) else "|"
        right = str(C[i]) if i < len(C) else "|"
        print(f"{left}  {middle}  {right}")

def move(n, A, B, C):
    if n == 1:
        disk = rods[A].pop()
        rods[C].append(disk)
        print(f"move {disk} from  {A} to {C}")
        display_rods(rods['A'], rods['B'], rods['C'])
    else:
        move(n-1, A, C, B)   # move n-1 disks
        move(1, A, B, C)     # move biggest
        move(n-1, B, A, C)   # move n-1 disks


n = int(input("Enter Input : "))
rods = {'A': list(range(n, 0, -1)), 'B': [], 'C': []}

display_rods(rods['A'], rods['B'], rods['C']) 
move(n, 'A', 'B', 'C')
