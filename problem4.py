def is_palindrome(n):
	orig = n
	rev = 0
	while n != 0:
		rev = rev*10 + n%10
		n //= 10
	return rev == orig

largest_pal_prod = 0
for i in reversed(range(100, 1000)):
	for j in reversed(range(i, 1000)):
		p = i*j
		if p>largest_pal_prod and is_palindrome(p):
			largest_pal_prod = p
		if p<largest_pal_prod:
			break

print largest_pal_prod
