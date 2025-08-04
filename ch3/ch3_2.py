inp = input("Enter expresion : ")
stack = []
opening_brackets = "([{"
closing_brackets = ")]}"
bracket_map = {')': '(', ']': '[', '}': '{'}

for char in inp:
    if char in opening_brackets:
        stack.append(char)
    elif char in closing_brackets:
        if not stack:
            print(f"{inp} close paren excess")
            break
        if stack[-1] != bracket_map[char]:
            print(f"{inp} Unmatch open-close")
            break
        stack.pop()
else:
    if stack:
        print(f"{inp} open paren excess   {len(stack)} : {''.join(stack)}")
    else:
        print(f"{inp} MATCH")
        
