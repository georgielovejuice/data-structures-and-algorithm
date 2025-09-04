class Node:
    def __init__(self, data):
        self.data = data 
        self.next = None
        self.previous = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        data = str(data)
        new_node = Node(data)
        if not self.head:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.previous = self.tail
            self.tail = new_node

    def insert_head(self, data):
        data = str(data)
        new_node = Node(data)
        if not self.head:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.previous = new_node
            self.head = new_node

    def insert(self, index, data):
        data = str(data)
        if index < 0:
            print("Data cannot be added")
            return
        if index == 0:
            self.insert_head(data)
            print(f"index = {index} and data = {data}")
            return

        current = self.head
        pos = 0
        while current and pos < index - 1:
            current = current.next
            pos += 1

        if current is None:
            print("Data cannot be added")
            return

        new_node = Node(data)
        new_node.next = current.next
        new_node.previous = current
        if current.next:
            current.next.previous = new_node
        current.next = new_node

        if new_node.next is None:
            self.tail = new_node

        print(f"index = {index} and data = {data}")

    def remove(self, data):
        data = str(data)
        current = self.head
        index = 0
        while current:
            if current.data == data:
                if current.previous:
                    current.previous.next = current.next
                else:
                    self.head = current.next
                if current.next:
                    current.next.previous = current.previous
                else:
                    self.tail = current.previous
                print(f"removed : {data} from index : {index}")
                return
            current = current.next
            index += 1
        print("Not Found!")

    def remove_at_index(self, index):
        if index < 0:
            print("Not Found!")
            return
        current = self.head
        pos = 0
        while current:
            if pos == index:
                data = current.data
                if current.previous:
                    current.previous.next = current.next
                else:
                    self.head = current.next
                if current.next:
                    current.next.previous = current.previous
                else:
                    self.tail = current.previous
                print(f"removed : {data} from index : {index}")
                return
            current = current.next
            pos += 1
        print("Not Found!")

    def display(self):
        current = self.head
        elements = []
        while current:
            elements.append(current.data)
            current = current.next
        return "linked list : " + "->".join(elements)

    def display_reverse(self):
        current = self.tail
        elements = []
        while current:
            elements.append(current.data)
            current = current.previous
        return "reverse : " + "->".join(elements)


def main():
    input_data = input("Enter Input : ").split(",")
    dll = DoublyLinkedList()

    for command in input_data:
        parts = command.strip().split()
        if parts[0] == 'A':
            dll.append(parts[1])
        elif parts[0] == 'I':
            index, value = parts[1].split(":")
            dll.insert(int(index), value)
        elif parts[0] == 'R':
            dll.remove(parts[1])
        elif parts[0] == 'Ri':
            dll.remove_at_index(int(parts[1]))
        elif parts[0] == 'Ab':
            dll.insert_head(parts[1])

        print(dll.display())
        print(dll.display_reverse())

if __name__ == "__main__":
    main()
