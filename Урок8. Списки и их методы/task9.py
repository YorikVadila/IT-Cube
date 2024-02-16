a = input()
b = input()
x = []
x.extend(a)
print(x)
for i in range(1, len(x) * 2 - 1, 2):
    x.insert(i, b)
print(x)
