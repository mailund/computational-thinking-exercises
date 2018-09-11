# The Sieve of Eratosthenes

The [Sieve of Eratosthenes](https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes) is an early algorithm for computing all prime numbers less than some upper bound $n$. It works as follows: we start with a set of candidates for numbers that could be primes, and since we do not a priori know which numbers will be primes we start with all the natural numbers from two and up to $n$.

```python
candidates = list(range(2, n + 1))
```

We are going to figure out which are primes by elimination and put the primes in another list that is initially empty.

```python
primes = []
```

The trick now is to remove from the candidates the numbers we know are not primes. We will require the following loop invariants:

1. All numbers in `primes` are prime.
2. No number in `candidates` can be divided by a number in `primes`.
3. The smallest number in `candidates` is a prime.

**Exercise:** Prove that the invariants are true with the initial lists defined as above.

We will now loop as long as there are candidates left. In the loop, we take the smallest number in the `candidates` list, which by the invariant must be a prime. Call it $p$. We then remove all candidates that are divisible by $p$ and then add $p$ to `primes`.

**Exercise:** Prove that the invariants are satisfied after these steps whenever they are satisfied before the steps.

**Exercise:** Prove that this algorithm terminates and is correct, i.e., that `primes` once the algorithm terminates contain all primes less than or equal to $n$. Correctness does not follow directly from the invariants so you might have to extend them.

**Exercise:** Implement and test this algorithm.


You can find my answer [here](answers.md)
