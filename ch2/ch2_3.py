def RANGE(*args):
    if len(args) == 1:
        start = 0.0
        end = args[0]
        step = 1.0
    elif len(args) == 2:
        start = args[0]
        end = args[1]
        step = 1.0
    elif len(args) == 3:
        start = args[0]
        end = args[1]
        step = args[2]
    else:
        raise ValueError("Invalid number of arguments")

    result = []
    if step > 0:
        while start < end:
            result.append(start)
            start += step
    else:
        while start > end:
            result.append(start)
            start += step

    result_tuple = tuple(result)

    return result_tuple

print('*** New Range ***')
n = [float(i) for i in input('Enter Input : ').split()]
if len(n) == 1:
    k = RANGE(n[0])
    print(RANGE(n[0]))
elif len(n) == 2:
    print(RANGE(n[0], n[1]))
elif len(n) == 3:
    print(tuple(round(x, 3) for x in RANGE(n[0], n[1], n[2])))