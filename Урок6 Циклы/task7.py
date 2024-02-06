a = input()
x = []
for i in a:
    if int(i) % 2 == 0:
        i = str(i)
        x.append(i)
        for k in range(len(x)):
            if type(x[k]) == str:
                k = int(k)
print(max(x))
#сделано