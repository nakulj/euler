n = 600851475143
candidates = range(2, int(n ** 0.5))
l = len(candidates)

flags = [False] * l
# flag the composites as they are found

for i in xrange(l):
	if flags[i]:
		continue
	for j in xrange(i+candidates[i], l, candidates[i]):
		flags[j] = True

for i in reversed(xrange(l)):
	if n%candidates[i] == 0 and not flags[i]:
		print candidates[i]
		break
