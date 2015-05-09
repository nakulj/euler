def sieve(n):
	if n < 2:
		return []
	candidates = range(2, n+1)
	primes = []
	while(len(candidates) > 0):
		next_prime = candidates[0]
		primes.append(next_prime)
		candidates = filter(lambda x: x%next_prime != 0, candidates)
	return primes
