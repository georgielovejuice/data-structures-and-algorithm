inp = input("Enter Input : ")
stack = []
num = 0 
for i in inp:
    if i == '(' or i == '[':
        stack.append(i)
    elif i == ')' or i == ']':
        if stack and ((stack[-1] == '(' and i == ')') or (stack[-1] == '[' and i == ']')):
            stack.pop()
        else:
            num += 1 # unbalanced closing bracket
    else:
        num += 1 #any other character

result = num + len(stack)

if result == 0:
    print(result, "\nPerfect ! ! !")
else:
    print(result)
