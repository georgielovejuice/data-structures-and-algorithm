class Queue:
    def __init__(self, input_data = None):
        self.queue = []
        self.data = [part.split() for part in input_data]

    def isEmpty(self):
        return len(self.queue) == 0

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if not self.isEmpty():
            return self.queue.pop(0)
        return ("-1")

    def size(self):
        if self.isEmpty():
            return "0"
        return len(self.queue)

    def run(self):
        for _, item in enumerate(self.data):
            if item[0] == "E":
                self.enqueue(item[1])
                print(f"Add {item[1]} index is {len(self.queue) - 1}")
            elif item[0] == "D":
                removed_item = self.dequeue()
                if removed_item == "-1":
                    print("-1")
                else:
                    print(f"Pop {removed_item} size in queue is {self.size()}")
        if self.queue:
            print(f"Number in Queue is :   {self.queue}")
        else:
            print(f"Empty")




input_data = input("Enter Input : ").split(',')
queue = Queue(input_data)
queue.run()
