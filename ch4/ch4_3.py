class Bank:

    def __init__(self, input_data=None):
        self.queue = []
        self.data = [part.strip().split() for part in input_data]

    def isEmpty(self):
        return len(self.queue) == 0

    def enqueue(self, name, customer_type):
        if customer_type == "VIP":
            insert_index = 0
            for index, (_, type) in enumerate(self.queue):
                if type == "VIP":
                    insert_index = index + 1
            self.queue.insert(insert_index, (name, customer_type))
        else:
            self.queue.append((name, customer_type))

    def dequeue(self):
        if not self.isEmpty():
            return self.queue.pop(0)
        return None

    def size(self):
        return len(self.queue)

    def run(self):
        for item in self.data:
            if item[0] == "ARRIVE":
                self.enqueue(item[1], item[2])
            elif item[0] == "SERVE":
                if self.isEmpty():
                    print("No customers.")
                else:
                    served = self.dequeue()
                    print(f"Served: {served[0]}") 
            elif item[0] == "VIEW":
                if self.isEmpty():
                    print("Queue: Empty.")
                else:
                    name_in_queue = [name for name, _ in self.queue]
                    print(f"Queue: {name_in_queue}")
            else:
                print("Exiting.")

input_data = input("Input: ").split(";")
bank = Bank(input_data)
bank.run()