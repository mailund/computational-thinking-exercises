n = 20
candidates = list(range(2, n+1))
primes = []
while len(candidates) > 0:
    p = candidates[0]
    candidates = [m for m in candidates if m % p != 0]
    primes.append(p)
print(primes)
