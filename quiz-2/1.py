def find_max(lst): 
    if len(lst) == 1:
        return lst[0]
    else:
        max_of_rest = find_max(lst[1:])
        if max_of_rest > lst[0]:
            return max_of_rest
        else:
            return lst[0]

inp = input('Enter Number list : ').split()
inp = [int(e) for e in inp]
print("max :", find_max(inp)) 