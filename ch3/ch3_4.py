class Calculator:
    
    def __init__(self):
        self.stack = []
    
    def run(self, input_expression):
        input_expression = input_expression.split()

        for char in input_expression:
            if char.isdigit():
                self.stack.append(int(char))
            elif char == "+":
                if len(self.stack) < 2:
                    return "Invalid instruction: +"
                a, b = self.stack.pop(), self.stack.pop()
                self.stack.append(b + a)
            elif char == "-":
                if len(self.stack) < 2:
                    return "Invalid instruction: -"
                a, b = self.stack.pop(), self.stack.pop()
                self.stack.append(a - b)
            elif char == "*":
                if len(self.stack) < 2:
                    return "Invalid instruction: *"
                a, b = self.stack.pop(), self.stack.pop()
                self.stack.append(b * a)
            elif char == "/":
                if len(self.stack) < 2:
                    return "Invalid instruction: /"
                a, b = self.stack.pop(), self.stack.pop()
                if a == 0:
                    return "Invalid instruction: Cannot divide by zero"
                self.stack.append(a // b)
            elif char == "^":
                if len(self.stack) < 2:
                    return "Invalid instruction: ^"
                a, b = self.stack.pop(), self.stack.pop()
                self.stack.append(b ** a)
            elif char == "DUP":
                if not self.stack:
                    return "Invalid instruction: DUP"
                self.stack.append(self.stack[-1])
            elif char == "POP":
                if not self.stack:
                    return "Invalid instruction: POP"
                self.stack.pop()
            elif char == "PSH":
                if not self.stack:
                    return "Invalid instruction: PSH"
                self.stack.append(self.stack[-1])
            else:
                return f"Invalid instruction: {char}"
        return self.stack[-1] if self.stack else 0
    
print("* Stack Calculator *")
input_data = input("Enter arguments : ")
calc = Calculator()
result = calc.run(input_data)
print(result)