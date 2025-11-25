a = float(input("Enter a first number: "))
b = float(input("Enter second number: "))
res = (a % b == 0) or (b % a == 0)
print(int(res))