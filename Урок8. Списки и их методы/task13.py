n = map(int, input().split())
x = [i ** 2 for i in n if i % 10 != 4 and i % 2 == 0]
print(*x)
