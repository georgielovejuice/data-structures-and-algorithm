class ParkingLot:
    '''
    first position is the maximum number of cars that can park in Mr. A's alley
    the second position is the car currently parked in Mr. A's alley
    the third position is the action (e.g., if it is "arrive", it will add a car to the alley, and if it is "depart", it will remove a car from the alley)
    the fourth position is the number of the car to be added or removed
    '''
    def __init__(self, maximum, soi, operation):
        self.maximum = int(maximum)
        op_partition = operation.strip().split()
        self.operation = op_partition[0] if op_partition else ''
        self.car_number = int(op_partition[1]) if len(op_partition) > 1 else None
        self.stack = [int(x) for x in soi.split(',')]

    def run(self):
        if self.operation == 'arrive':
            if len(self.stack) >= self.maximum:
                print(f"car {self.car_number} cannot arrive : Soi Full")
            elif self.car_number in self.stack:
                print(f"car {self.car_number} already in soi")
            else:
                self.stack.append(self.car_number)
                print(f"car {self.car_number} arrive! : Add Car {self.car_number}")

        elif self.operation == 'depart':
            if self.car_number in self.stack:
                self.stack.remove(self.car_number)
                print(f"car {self.car_number} depart ! : Car {self.car_number} was remove")
            else:
                print(f"car {self.car_number} cannot depart : Dont Have Car {self.car_number}")

        print(self.stack if self.stack else [])

print("******** Parking Lot ********")
max_car, soi_car, op = [part.strip() for part in input("Enter max of car / car in soi / operation : ").split('/')]
parking_lot = ParkingLot(max_car, soi_car, op)
parking_lot.run()
