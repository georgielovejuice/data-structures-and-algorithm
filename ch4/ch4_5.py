class Queue:
    def __init__(self, items=None):
        self.items = items if items else []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        return self.items.pop(0) if not self.isEmpty() else None

    def isEmpty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

class CandyCrush:
    def __init__(self, normal_side, mirror_side):
        self.mirror_side = mirror_side
        self.normal_side = normal_side

    def collapse_mirror_side(self, mirror_side):
        reversed_input = mirror_side[::-1]
        stack = []
        exploded_queue = Queue()
        explosion_count = 0
        changed = True

        while changed:
            changed = False
            i = 0
            while i < len(reversed_input):
                if not stack:
                    stack.append([reversed_input[i], 1])
                else:
                    if stack[-1][0] == reversed_input[i]:
                        stack[-1][1] += 1
                    else:
                        if stack[-1][1] >= 3:
                            while stack[-1][1] >= 3:
                                exploded_queue.enqueue(stack[-1][0])
                                explosion_count += 1
                                stack[-1][1] -= 3
                                changed = True
                            if stack[-1][1] == 0:
                                stack.pop()
                            continue
                        else:
                            stack.append([reversed_input[i], 1])
                i += 1

            if stack and stack[-1][1] >= 3:
                while stack[-1][1] >= 3:
                    exploded_queue.enqueue(stack[-1][0])
                    explosion_count += 1
                    stack[-1][1] -= 3
                    changed = True
                if stack[-1][1] == 0:
                    stack.pop()

            reversed_input = ''.join(char * count for char, count in stack)
            stack.clear()

        final_mirror = reversed_input[::-1]
        return exploded_queue, final_mirror, explosion_count

    def collapse_normal_side(self, normal_side, mirror_queue):
        stack = []
        explosion_count = 0
        failed_block = 0

        i = 0
        while i < len(normal_side):
            current = normal_side[i]

            if not stack:
                stack.append([current, 1])
            else:
                if stack[-1][0] == current:
                    stack[-1][1] += 1

                    if stack[-1][1] == 3:
                        if not mirror_queue.isEmpty():
                            block_char = mirror_queue.dequeue()

                            if block_char == current:
                                stack[-1][1] = 1
                                failed_block += 1
                            else:
                                char = stack[-1][0]
                                stack.pop()
                                stack.append([char, 2])
                                if stack[-1][0] == block_char:
                                    stack[-1][1] += 1
                                else:
                                    stack.append([block_char, 1])
                                if stack[-1][0] == char:
                                    stack[-1][1] += 1
                                else:
                                    stack.append([char, 1])
                        else:
                            stack.pop()
                            explosion_count += 1
                else:
                    if stack[-1][1] >= 3:
                        explosion_count += 1
                        stack.pop()
                        i -= 1 
                    else:
                        stack.append([current, 1])
            i += 1

        if stack and stack[-1][1] >= 3:
            explosion_count += 1
            stack.pop()

        result = ''.join(char * count for char, count in stack)
        return failed_block, result[::-1], explosion_count


    def run(self):
        mirror_queue, mirror_remaining, mirror_exploded_count = self.collapse_mirror_side(self.mirror_side)
        failed_bomb_block, normal_remaining, normal_exploded_count = self.collapse_normal_side(self.normal_side, mirror_queue)

        print("NORMAL :")
        print(len(normal_remaining))
        print(normal_remaining if normal_remaining else "Empty")
        print(normal_exploded_count, "Explosive(s) ! ! ! (NORMAL)")
        if failed_bomb_block > 0:
            print("Failed Interrupted", failed_bomb_block, "Bomb(s)")

        print("------------MIRROR------------")
        print(": RORRIM")
        print(len(mirror_remaining))
        print(mirror_remaining if mirror_remaining else "ytpmE")
        print("(RORRIM) ! ! ! (s)evisolpxE", mirror_exploded_count)

def main():
    normal_side, mirror_side = input("Enter Input (Normal, Mirror) : ").split(" ")
    candycrush = CandyCrush(normal_side, mirror_side)
    candycrush.run()

if __name__ == "__main__":
    main()
