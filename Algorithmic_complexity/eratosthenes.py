
n = 15

def eratosthenes1(n):
    access = 0
    candidates = list(range(2, n + 1))
    primes = []
    while candidates:
        p = candidates[0] ; access += 1
        primes.append(p)
        access += len(candidates)
        candidates = [x for x in candidates if x % p != 0]
    return access, primes

from math import sqrt
def eratosthenes2(n):
    access = 0
    candidates = list(range(n + 1))
    access += 2
    candidates[0], candidates[1] = None, None

    for i in range(int(sqrt(n) + 1)):
        access += 1
        if candidates[i] is None:
            continue

        # Sieve..., time O(n/p)
        access += 1
        p = candidates[i]
        # p squared is the first place we find a number that
        # p divides, after p itself
        for j in range(p**2, n + 1, p):
            access += 1
            candidates[j] = None

    primes = [p for p in candidates if p is not None]
    access += len(primes)
    return access, primes

for n in range(100, 2000):
    n1, primes1 = eratosthenes1(n)
    n2, primes2 = eratosthenes2(n)
    assert primes1 == primes2
    print(n, n1, n2)
