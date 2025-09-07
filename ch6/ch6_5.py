def staircase(n, step=1):
    if n > 0: # positive
        if step > n:
            return "===== End of program ====="
        return "_" * (n - step) + "#" * step + "\n" + staircase(n, step + 1) # start from first floor
    if n < 0: # negative
        n = abs(n)
        if step > n:
            return "===== End of program ====="
        return "_" * (step - 1) + "#" * (n - step + 1) + "\n" + staircase(-n, step + 1) # start from last floor and flip
    else:
        return ("Not Draw!" + "\n" + "===== End of program =====")

print(" *** Stair case ***")
print(staircase(int(input("Enter Input : "))))

