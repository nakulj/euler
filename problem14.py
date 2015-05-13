import common

def jump(n):
	if n%2==0:
		return n/2
	else:
		return 3*n +1

@common.cached
def countJumps(n):
	if n is 1:
		return 1
	return 1 + countJumps(jump(n))

max_jumps = 1
n = 1

for i in range(2, 10**6):
	jumps = countJumps(i)
	if jumps>max_jumps:
		max_jumps= jumps
		n = i

print n