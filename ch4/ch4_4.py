class Queue:
    
    def __init__(self, items = None):        
        self.items = items

    def isEmpty(self):
        return len(self.queue) == 0

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.isEmpty():
            return self.items.pop(0)
        return None

    def size(self):
        return len(self.items)

    def __str__(self):
        return f"{self.items}"

    def 
print(" ***Cafe***")
log = input("Log : ").split("/")
print(log)
         