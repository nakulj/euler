primes_list = [2]
i = 3

while len(primes_list) < 10001:
    for p in primes_list:
        if i % p == 0:
            break
    else:
        primes_list.append(i)
    i += 2

print primes_list[-1]