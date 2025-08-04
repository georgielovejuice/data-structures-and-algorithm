input = input("Enter Infix : ")
input = input.replace(" ", "")
stack = []
postfix = []
precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}

for char in input:
    if char.isalnum():  # Check char is it letter or operator
        postfix.append(char)
    elif char == '(':
        stack.append(char)
    elif char == ')':
        while stack and stack[-1] != '(':
            postfix.append(stack.pop())
        if stack:
            stack.pop() # pop '(' from the stack
    else: # Operator
        while (stack and stack[-1] != '(' and 
               (precedence[char] < precedence[stack[-1]] or 
                (precedence[char] == precedence[stack[-1]] and char != '^'))):
            postfix.append(stack.pop())
        stack.append(char)

while stack:
    postfix.append(stack.pop()) # Pop operator from the stack

result = ''
for char in postfix:
    result += char
print(f"Postfix : {result}")