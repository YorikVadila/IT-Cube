n = int(input())
if n <= 2:
    print(n * 10.5)
else:
    print( ((n - (n - 2)) * 10.5) + ((n - 2)) * 4 )
    