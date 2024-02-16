a = "abcdefghijklmnopqrstuvwxyz"
x = []
for i in range(0,27):
    for j in range(i):
        x.extend(a[i-1])
print(x)
s = " ".join(x)
print(s)
#получилось только так