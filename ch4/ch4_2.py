class Queue:
    def __init__(self, input_data):
        self.main = input_data
        self.cashier1 = []
        self.cashier2 = []
        
    def run(self):
        minute = 0
        while self.main:
            minute += 1
            '''
            1 % 3 = 1, 2 % 3 = 2, 3 % 3 = 0, 4 % 3 = 1... countinue like this with (1 2 0) pattern. So,
            It will remove when minute = start at 1, 4, 7, 10, ... or It is minute % 3 == 0 and + 1 same as the testcase.
            '''
            if minute % 3 == 1 and self.cashier1: 
                self.cashier1.pop(0)  

            if minute % 2 == 0 and self.cashier2:
                self.cashier2.pop(0)

            if self.main:
                person = self.main.pop(0)
                if len(self.cashier1) < 5:
                    self.cashier1.append(person)
                elif len(self.cashier2) < 5:
                    self.cashier2.append(person)

            print(f"{minute} {self.main} {self.cashier1} {self.cashier2}")

input_data = [str(part) for part in input("Enter people : ")]
queue = Queue(input_data)
queue.run()