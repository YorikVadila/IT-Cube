import math
a = float(input())
b = float(input())
c = float(input())
discr = b ** 2 - 4 * a * c
if discr > 0:
    x1 = (-b + math.sqrt(discr)) / (2 * a)
    x2 = (-b - math.sqrt(discr)) / (2 * a)
    print(x1)
    print(x2)
elif discr == 0:
    x = -b / (2 * a)
    print(x)
else:
    print("Корней нет")