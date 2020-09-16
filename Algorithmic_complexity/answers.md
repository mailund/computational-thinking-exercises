# Answers for "Algorithmic Efficiency"

## Counting primitive operations

### Exercise

Consider this way of computing the mean of a sequence of numbers:

```python
accumulator = 0
for n in numbers:
	accumulator += n
mean = accumulator / len(numbers)
```

Count how many primitive operations it takes. To do it correctly you need to distinguish between updating a variable and assigning a value to a new one. Updating the accumulator `accumulator += n` usually maps to a single operation on a CPU because it involves changing the value of a number that is most likely in a register. Assigning to a new variable, as in

```python
mean = accumulator / len(numbers)
```

doesn’t update `accumulator` with a new value, rather it needs to compute a division, which is one operation (and it needs `len(numbers)` before it can do this, which is another operation), and then write the result in a new variable, which is an additional operation.

### Answer

```python
accumulator = 0                      # 1
for n in numbers:                    # 5 × n + 2
	accumulator += n                   # n × 1
mean = accumulator / len(numbers)    # 3
```

so (5 + 1) × n + (1 + 2 + 3) =  6 × (n + 1).

### Exercise

Consider this alternative algorithm for computing the mean of a sequence of numbers:

```python
accumulator = 0
length = 0
for n in numbers:
	accumulator += n
	length += 1
mean = accumulator / length
```

How many operations are needed here? Is it more or less efficient than the previous algorithm?

```python
accumulator = 0                  # 1
length = 0                       # 1
for n in numbers:                # 5 × n + 2
	accumulator += n               # 1 × n
	length += 1                    # 1 × n
mean = accumulator / length      # 3
```

This implementation uses (5 + 1 + 1) × n + (1 + 1 + 2 + 3) = 7 × (n + 1). It is less efficient.



## Guessing-game complexity

**Exercise:** Identify the best- and worst-case scenarios for each strategy and derive the best-case and worst-case time usage.

### Answer

For the first strategy, the best case is when 1 is the value we are looking for and the worst case is when it is 20. The best-case and worst-case running times are O(1) and O(n).

For the second strategy, the best case is when we are looking for 20 and the worst case is when we are looking for 1. The best- and worst-case running times are O(1) and O(n).

For the third strategy, the best case is if we are looking for 10 (the first mid-point). In that case the running time is O(1). The worst case is when the value we are searching for is not the mid-point until there is only one element left. There are many ways that this can happen, but in all case we find the value in time O(log n), which is the worst-case complexity. We get this running time because we remove half of the range in each iteration, and if we remove half the elements in each iteration we cannot have more than log₂ n iterations before there is only one element left.


## Function growth

Classes 

1. O(log n), o(log n), Ω(log n) and ⍵(log n)
3. O(n), o(n), Ω(n), and ⍵(n)
4. O(n²), o(n²), Ω(n²), and ⍵(n²)
5. O(2ⁿ), o(2ⁿ), Ω(2ⁿ), ⍵(2ⁿ)

Functions:

1. f(n) = 23 × n
	1. Ω(log n) and ⍵(log n)
	2. O(n) and Ω(n)
	3. O(n²) and o(n²)
	4. O(2ⁿ) and o(2ⁿ)

2. f(n) = 42 × n² - 100 × n
	1. Ω(log n) and ⍵(log n)
	2. Ω(n) and ⍵(n)
	3. O(n²) and Ω(n²)
	4. O(2ⁿ) and o(2ⁿ)

3. f(n) = n / log(n)
	1. Ω(log n) and ⍵(log n)
	2. O(n), o(n)
	3. O(n²) and o(n²)
	4. O(2ⁿ) and o(2ⁿ)

4. f(n) = log(n) / n
	1. O(log n) and o(log n)
	2. O(n) and o(n)
	3. O(n²) and o(n²)
	4. O(2ⁿ) and o(2ⁿ)

5. f(n) = n²/log(n)
	1. Ω(log n) and ⍵(log n)
	2. Ω(n), and ⍵(n)
	3. O(n²) and o(n²)
	4. O(2ⁿ) and o(2ⁿ)

6. f(n) = log(n) + log(n)/n
	1. O(log n) and Ω(log n)
	2. O(n) and o(n)
	3. O(n²) and o(n²)
	4. O(2ⁿ) and o(2ⁿ)

7. f(n) = 5ⁿ - n³
	1. Ω(log n) and ⍵(log n)
	2. Ω(n) and ⍵(n)
	3. Ω(n²) and ⍵(n²)
	4. Ω(2ⁿ) and ⍵(2ⁿ)

8. f(n) = n!
	1. Ω(log n) and ⍵(log n)
	2. Ω(n) and ⍵(n)
	3. Ω(n²) and ⍵(n²)
	4. Ω(2ⁿ) and ⍵(2ⁿ)

9. f(n) = 2ⁿ/n
	1. Ω(log n) and ⍵(log n)
	2. Ω(n) and ⍵(n)
	3. Ω(n²) and ⍵(n²)
	4. O(2ⁿ) and o(2ⁿ)

10. f(n) = log(log(n))
	1. O(log n) and o(log n)
	2. O(n) and o(n)
	3. O(n²) and o(n²)
	4. O(2ⁿ) and o(2ⁿ)



## Sieve of Eratosthenes

**Exercise:** Derive an upper bound for its running time. 

**Answer:** For each i=1,…,n we potentially iterate through all larger numbers j=i+1,…n. On average this means that we iterate through n/2 numbers for each i, so an upper bound is O(n²).

**Exercise:** Is there a difference between its best-case and worst-case running time?

**Answer:** No, in the sense that there is not data that gives us better or worse running time.

However, the running time is not quadratic as we just derived; the algorithm runs faster than that. It *is* O(n²), because it is an upper bound; we do not compare more than quadratically many numbers, but it is not a tight upper bound. We do not *actually* iterate through all numbers larger than i. Only those that we have not eliminated as divisible by a number smaller than i. Getting the average number of elements left in the list when we look at prime p is not so straightforward; at least not to me.

We can modify the algorithm slightly, to make it easier to reason about. Instead of running through all the candidates in each inner loop, we can jump through the multiples of the current prime. If we keep all candidates in the list when we "remove" them, and merely tag them as removed, we can jump in steps of p to do this.

This is easiest to do if the indices into candidates match the numbers, so we start with zero. Since 0 and 1 are not prime, we can tag them as such immediately; set them to `None`. Then you move through the candidates list, continue when you see a tagged number, and when you find a prime, jump through the list and tag the multiples of it.

```python
candidates = list(range(n + 1))
candidates[0], candidates[1] = None, None
for i in range(n + 1):
    if candidates[i] is None:
        continue

    # Sieve..., time O(n/p)
    p = candidates[i]
    # skip index i, that is the prime we want to keep
    for j in range(i + p, n + 1, p):
        candidates[j] = None

primes = [p for p in candidates if p is not None]
```


If you implement the algorithm this way, you can reason that the running time is n plus the total running time of the inner loop. The inner loop, when you look at prime p, has n/p steps (you jump up to n in step sizes of p). So, an upper bound of the algorithm is O(n + n/2 + n/3 + n/5 + … ) or O(n + n × (sum of 1/p for primes less than n).

The sum here is called the "sum of reciprocals of primes", and it is shown to be in O(log(log(n)). So, a tighter bound on the running time is O(n × log(log(n)))--if we use the second version.

In the first algorithm, we do not consider candidates that we have already eliminated, but in the second we do. On the other hand, in the first algorithm we do not skip past candidates we know are not multiples of the prime we are sieving no, while in the second we do. I do not know which algorithm is the fastest. Someone certainly will, but it is not obvious to me. Experimentally, however, I find that the second algorithm accesses the list substantially fewer time. I suspect that continues being the case to larger numbers than those I have tried, but when it comes to primes you know know what they get up to a few numbers higher than where you looked...


## Merging

I don’t know how you implemented the merge algorithm, but my solution looks like this:

```python
n, m = len(x), len(y)
i, j = 0, 0
z = []

while i < n and j < m:
        if x[i] < y[j]:
                z.append(x[i])
                i += 1
        else:
                z.append(y[j])
                j += 1

if i < n:
        z.extend(x[i:])
if j < m:
        z.extend(y[j:])
```

The two `extend` calls run in linear time (you have to trust me that it does; it is built into Python’s list implementation). So we only need to concern ourselves with the `while`-loop. Here, the body of the loop runs in constant time—appending to a list is a constant time operation. In each iteration we increment either `i` or `j`, so the total number of iterations is bounded by `n + m`.
