a = int(input())
b = int(input())
c = int(input())
if a < 0:
    print(b + c)
if b < 0:
    print(a + c)
if c < 0:
    print(a + b)
if a < 0 and b < 0:
    print(c)
if a < 0 and c < 0:
    print(b)
if b < 0 and c < 0:
    print(a)
if a < 0 and b < 0 and c < 0:
    print("Все числа отрицательные")  
else:
    print(a + b + c)
