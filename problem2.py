f1, f2 = 1, 2
sum_evens = 0

while f1 <= 4000000:
	if f1 % 2 == 0:
		sum_evens += f1
	f1, f2 = f2, f1 + f2

print sum_evens
