def length(txt):
    if txt == "":
        return 0
    return 1 + length(txt[1:])

def sep(txt, index=1):
    if txt == "":
        return ""
    
    if index % 2 == 1:
        return txt[0] + "*" + sep(txt[1:], index + 1)
    else:
        return txt[0] + "~" + sep(txt[1:], index + 1)

print(" *** Length of string (Recursion) ***")
input = input("Enter Input : ")
print(sep(input))
print(f"length of '{input}' is {length(input)}")
    
