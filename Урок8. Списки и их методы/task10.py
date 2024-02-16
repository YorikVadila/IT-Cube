x = input().split()
mx = max(x)
mn = min(x)
imx = x.index(mx)
imn = x.index(mn)
x[imx], x[imn] = x[imn], x[imx]
print(*x)