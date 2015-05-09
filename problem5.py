from common import sieve

N = 20

lst = range(1, N+1)
primes = sieve(N)
lcm = 1

for prime in primes:
	while(True):
		found_a_multiple = False
		for i, n in enumerate(lst):
			if n%prime == 0:
				lst[i] /= prime
				found_a_multiple = True
		if found_a_multiple:
			lcm *= prime
		else:
			break

print lcm
