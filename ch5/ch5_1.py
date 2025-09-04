class Node:

    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def insert_head(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def delete(self, data):
        if not self.head:
            return
        if self.head.data == data:
            self.head = self.head.next
            return
        current_node = self.head
        while current_node.next and current_node.next.data != data:
            current_node = current_node.next
        if current_node.next:
            current_node.next = current_node.next.next

    def print_list(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end=' ')
            if current_node.next:
                print("->", end=' ')
            current_node = current_node.next
        print("-> None")

def main():
    input_data = input("Enter Commands: ").split()
    linked_list = LinkedList()
    i = 0

    while i < len(input_data):
        command = input_data[i]
        if command == "append":
            i += 1
            linked_list.append(input_data[i])
        elif command == "insert_head":
            i += 1
            linked_list.insert_head(input_data[i])
        elif command == "delete":
            i += 1
            linked_list.delete(input_data[i])
        elif command == "print":
            linked_list.print_list()
        i += 1

if __name__ == "__main__":
    main()