x = input().split()
mx = max(x, key=len)
mn = min(x, key=len)
imx = x.index(mx)
imn = x.index(mn)
x[imx], x[imn] = x[imn], x[imx]
print(*x)