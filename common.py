def sieve(n):
	if n<2:
		return
	
	is_prime = [True] * (n)
	
	for i in range(2,n):
		if not is_prime[i]:
			continue
		yield i
		for j in range(2*i, n, i):
			is_prime[j] = False
