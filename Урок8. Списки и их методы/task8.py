a = input().split()
b = 0
a = list(map(int, a))
for j in range(len(a)):
    if a[j] > 50:
        b = b + 1
print(b)
