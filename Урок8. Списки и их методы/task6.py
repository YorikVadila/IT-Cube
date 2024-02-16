n = int(input())
x = []
for _ in range(n):
    a = input()
    x.append(a)
ff = x.count("first")
fs = x.count("second")
ft = x.count("third")
for i in range(ff - 1):
    x.remove("first")
for k in range(fs - 1):
    x.remove("second")
for j in range(ft - 1):
    x.remove("third")
print(*x, sep='\n')
#я без понятия как сделать вывод с любыми строками
