n = int(input())
st = [input() for _ in range(n)]
i = int(input())
x = [s[i-1] for s in st]
s1 = "".join(x)
print(s1)