a = int(input())
b = int(input())
c = int(input())
if a == b and a == c and b == c:
    print("Равносторонний")
if (a == c or a == b or b == c):
    print("Равнобедренный")
else:
    print("Разносторонний")