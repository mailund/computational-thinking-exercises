# The Sieve of Eratosthenes

I will require the following loop invariants:

1. All numbers in `primes` are prime.
2. No number in `candidates` can be divided by a number in `primes`.
3. The smallest number in `candidates` is a prime.

**Exercise:** Prove that the invariants are true with the initial lists defined as above.

> **Answer:** Any properties we care to require about the elements in an empty list are true. There are no elements for which they can be false. We call this *vacuously* true.

We will now look as long as there are candidates left. In the loop, we take the smallest number in the `candidates` list, which by the invariant must be a prime. Call it $p$. We then remove all candidates that are divisible by $p$ and then add $p$ to `primes`.

**Exercise:** Prove that the invariants are satisfied after these steps whenever they are satisfied before the steps.

> **Answer:** If the front element in `candidates` was divisible by any smaller number—and we only care about smaller numbers when we consider the divisible property—then it would have been removed. It isn’t divisible by a smaller number, it must therefore be prime. When we move it to `primes` we satisfy the invariant for that list. Let `p` be the first number in `candidates` before we move it to `primes`. In `candidates`, before we remove those divisible by `p`, we have no numbers that are divisible by any of the smaller primes. We explicitly remove those divisible by `p`. We are then left with numbers that are not divisible by any of the numbers in `primes`.

**Exercise:** Prove that this algorithm terminates and is correct, i.e., that `primes` once the algorithm terminates contain all primes less than or equal to $n$. Correctness does not follow directly from the invariants, so you might have to extend them.

> **Answer:** For a termination function we can use the length of the `candidates` list. It is decreased by at least one every iteration, because we move its first element to `primes`, and we terminate when it is empty. Where the invariants come up short is that they tell us that `primes` are all primes, as is `candidates[0]` when `candidates` is not empty, but they do not tell us that `primes` eventually will contain *all* the primes less than $n$. To get to there, we can modify the invariants to say that `primes` contain all primes less than `candidates[0]` when `candidates` is not empty or $n$ when it is. You can prove that this invariant is also true very similarly to how we proved the other invariants. When you have a prime in `p = candidates[0]`, `primes` contain all smaller primes (by the invariant). When we move `p` to `primes` the invariant is also true—`primes` still contain all primes less than `p`, this doesn’t change when we add `p`. From `candidates` we now remove numbers that are *not* prime, but never numbers that are. We end up with either a new `p = candidates[0]` that must be a larger prime, so we can repeat the argument for the next iteration, or we end up with an empty list. When we have an empty list we have evaluated all numbers up to and including $n$, and `primes` contain all the primes in that sequence.

**Exercise:** Implement and test this algorithm.

```python
candidates = list(range(2, n+1))
primes = []
while len(candidates) > 0:
    p = candidates[0]
    candidates = [m for m in candidates if m % p != 0]
    primes.append(p)
```

You can try out the implementation from [here](sieve.py)

