n = int(input())
b = 0
x = []
if n > 0:
    for i in range(1, n + 1):
        b = b + 1
        x.append(b)
    for j in range(n):
        print(x)
else:
    print("Ошибка!")