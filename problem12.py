from common import cached, prod
import itertools

class Sieve():
	def __init__(self):
		self.N = 2
		self.is_prime = [True]*2

	def sift(self, n):
		if n<=self.N:
			return [i for i in range(2, n) if self.is_prime[i]]
		N = max(n, self.N**2)
		self.is_prime += [True] * (N-self.N)
		for i in range(2, N):
			if not self.is_prime[i]:
				continue
			start = max(2, 1 + self.N//i)*i if i<N else 2*i
			for j in range(start, N, i):
				self.is_prime[j] = False
		self.N = N
		return [i for i in range(2, n) if self.is_prime[i]]

sieve = Sieve()

def add_factors(f1, f2):
	keys = set(f1) | set(f2)
	factors = {}
	for k in keys:
		factors[k] = f1.get(k,0) + f2.get(k,0)
	return factors

@cached
def prime_factorize(n):
	global sieve;
	if n == 1:
		return {}
	for p in sieve.sift(int(n**0.5)):
		if n%p == 0:
			return add_factors({p:1},prime_factorize(n//p))
	return {n:1}
	
def num_factors(f1, f2):
	f1 = prime_factorize(f1)
	f2 = prime_factorize(f2)
	return prod(v+1 for k,v in add_factors(f1, f2).items())

for i in itertools.count(1):
	factors = [(j/2 if j%2 == 0 else j) for j in i,i+1]
	if num_factors(*factors) > 500:
		print prod(factors)
		break
