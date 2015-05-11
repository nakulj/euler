def pairs_adding_to(n):
	for i in range(1, n//2 + 1):
		yield i, n-i

n = 1000

for c in range(1,n):
	for a,b in pairs_adding_to(n-c):
		if (a*a + b*b == c*c):
			print a*b*c
			break
	else:
		continue
	break
