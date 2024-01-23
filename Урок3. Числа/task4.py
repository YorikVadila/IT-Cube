a = int(input())
if a < 0:
    amin = a * -1
    a1 = amin // 100
    a25 = amin // 10
    a2 = a25 % 10
    a35  = amin % 10
    a3 = a35 % 10
    a1 = str(a1)
    a2 = str(a2)
    a3 = str(a3)
    print(a1+a2+a3)
    print(a1+a3+a2)
    print(a2+a1+a3)
    print(a2+a3+a1)
    print(a3+a1+a2)
    print(a3+a2+a1)
elif a > 0:
    amin = a * 1
    a1 = amin // 100
    a25 = amin // 10
    a2 = a25 % 10
    a35  = amin % 10
    a3 = a35 % 10
    a1 = str(a1)
    a2 = str(a2)
    a3 = str(a3)
    print(a1+a2+a3)
    print(a1+a3+a2)
    print(a2+a1+a3)
    print(a2+a3+a1)
    print(a3+a1+a2)
    print(a3+a2+a1)
