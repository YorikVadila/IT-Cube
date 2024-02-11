n = int(input())
a = 0
if n <= 0:
    print("Это отрицательное число!")
elif n == 0:
    print("Это число не имеет делителей!")
else:
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            if i % j == 0:
                a += 1
        print(f"{i} - {a} ")
