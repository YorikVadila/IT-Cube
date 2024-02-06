a = 0
x = []
while a != "СТОП":
    a = input()
    x.append(a)
    for k in range(len(x)):
        if type(x[k]) == str:
            k = int(k)
x.sort()            
x.pop(-1)
print(x[0,1,2])
#сложно