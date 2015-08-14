prod = 1
for n in xrange(1, 101):
	prod *= n
	while n % 10 == 0:
		n /= 10

s = 0
while prod > 0:
	s += prod % 10
	prod = prod // 10

print s
