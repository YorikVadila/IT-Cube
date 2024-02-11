n = int(input())
c = n
b = 0
if n < 0:
    print("Это отрицательно число!")
else:
    for i in range(1, n):
        n = n * i
        b = b + n
    print(b - c)