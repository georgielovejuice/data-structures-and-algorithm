class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.isEmpty():
            return self.items.pop(0)
        return None

    def __str__(self):
        if self.isEmpty():
            return "Empty"
        return " -> ".join([f"C{c.customer_number}" for c in self.items])


class Customer:
    def __init__(self, customer_number, enter_time, coffee_time):
        self.customer_number = customer_number
        self.enter_time = enter_time
        self.coffee_time = coffee_time
        self.wait_time = 0


class Coffeeshop:
    def __init__(self, log_input):
        self.all_customers = []
        for number, item in enumerate(log_input, 1):
            enter, coffee = map(int, item.split(","))
            self.all_customers.append(Customer(number, enter, coffee))

        self.waiting_queue = Queue()

        self.baristas = [None, None]
        self.baristas_time_left = [0, 0]

        self.max_wait_customer = None
        self.max_wait_time = -1
        self.finished_count = 0
        self.debug_mode = False # For debug kub
        self.someone_waited = False  # No one wait at first ja

    def debug(self, time):
        print(f"\n=== Debug at Time {time} ===")
        for b in range(2):
            if self.baristas[b] is None:
                print(f"Barista {b+1}: Free")
            else:
                print(f"Barista {b+1}: Serving customer {self.baristas[b].customer_number}, Time left {self.baristas_time_left[b]}")
        print(f"Queue: {self.waiting_queue}")

    def run(self):
        time = 0
        total_customers = len(self.all_customers)
        i = 0

        while self.finished_count < total_customers:

            if self.debug_mode:
                self.debug(time)

            while i < total_customers and self.all_customers[i].enter_time == time:
                self.waiting_queue.enqueue(self.all_customers[i])
                i += 1

            for b in range(2):
                if self.baristas[b] is None and not self.waiting_queue.isEmpty():
                    customer = self.waiting_queue.dequeue()
                    customer.wait_time = time - customer.enter_time

                    if customer.wait_time > 0:
                        self.someone_waited = True

                    if customer.wait_time > self.max_wait_time:
                        self.max_wait_time = customer.wait_time
                        self.max_wait_customer = customer

                    self.baristas[b] = customer
                    self.baristas_time_left[b] = customer.coffee_time

            finished_customers = []
            for b in range(2):
                if self.baristas[b] is not None:
                    self.baristas_time_left[b] -= 1

                    if self.baristas_time_left[b] == 0:
                        finished_customers.append(self.baristas[b])
                        self.baristas[b] = None
                        self.finished_count += 1
            
            finished_customers.sort(key=lambda customer: customer.customer_number)
            for customer in finished_customers:
                print(f"Time {time + 1} customer {customer.customer_number} get coffee")

            time += 1

        if self.someone_waited:
            print(f"The customer who waited the longest is : {self.max_wait_customer.customer_number}")
            print(f"The customer waited for {self.max_wait_time} minutes")
        else:
            print("No waiting")


def main():
    print(" ***Cafe***")
    log = input("Log : ").split("/")
    cafe = Coffeeshop(log)
    cafe.run()

if __name__ == "__main__":
    main()
