sum_multiples = 0
factors = [3,5]

for i in range(1000):
	for factor in factors:
		if i % factor == 0:
			sum_multiples += i
			break

print sum_multiples