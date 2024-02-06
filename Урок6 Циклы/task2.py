num = int(input())
b = 0
while num != 0:
	last_digit = num % 10
	if last_digit == 0:
		num = num // 10
		b = b + 1
	else:
		num //= 10
		continue
print(b)
#сделано

