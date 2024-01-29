a = int(input())
a3 = a % 10
a1 = a // 100
a25 = a // 10
a2 = a25 % 10
a1 = str(a1)
a2 = str(a2)
a3 = str(a3)
x = [a1,a2,a3]
x.sort()
mn = x[0] 
sr = x[1]
mx = x[2]
mn = int(mn)
sr = int(sr)
mx = int(mx)
otv = mx - mn
if otv == sr and 100 < a < 1000:
    print("Прикольное")
else: 
    print("Не прикольное")