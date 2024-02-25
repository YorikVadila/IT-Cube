a = int(input())
b = int(input())
c = input()
if c == "+":
    print(a + b)
if c == "-":
    print(a - b)
if c == "*":
    print(a * b)
if c == "/":
    if a or b != 0:
        print(a / b)
    else: print("На ноль делить нельзя!")
if c == "//":
    if a or b != 0:
        print(a // b)
    else: print("На ноль делить нельзя!")
if c == "**":
    print(a ** b)