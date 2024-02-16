n = int(input())
s = [input() for _ in range(n)]
ss = input()
f = [s1 for s1 in s if ss in s1]
for s in f:
    print(s)
