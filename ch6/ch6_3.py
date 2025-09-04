def gcd(num1, num2):
    """Greatest Common Divisor using Euclidean algorithm"""
    if num2 == 0:
        return num1
    return gcd(num2, num1 % num2)

num1, num2 = [int(input) for input in input("Enter Input : ").split()]
if num1 == 0 and num2 == 0:
    print("Error! must be not all zero.")
else:
    if num2 > num1:
        print(f"The gcd of {num2} and {num1} is : {abs(gcd(num1, num2))}")
    if num1 > num2:
        print(f"The gcd of {num1} and {num2} is : {abs(gcd(num2, num1))}")
