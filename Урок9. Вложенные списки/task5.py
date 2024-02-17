s = input()
x = [[s[0]]]
for i in s[1:]:
    if i == x[-1][-1]:
        x[-1].append(i)
    else:
        x.append([i])
x = [j for j in x if j != [' ']]
print(x)