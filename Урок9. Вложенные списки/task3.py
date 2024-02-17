x = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
s = sum(sum(i) for i in x)
c = sum(len(j) for j in x)
a = s / c
print(a)
