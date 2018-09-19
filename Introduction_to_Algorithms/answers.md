# Answers for “Introduction to Algorithms”

## Below or above

**Exercise:** Prove that all three strategies terminate and with the correct answer, i.e. they are algorithms for solving this problem.

> **Answer:** For 1: If you let `i` denote the current number you are considering, then 20 - `i` is your termination function. You never skip a number, so when you will eventually see all numbers between 1 and 20 and you will be told when you saw the right one.

> **Answer:** For 2: Here you can use `i` - 1 as your termination function (minus one to make the termination function hit zero at the last number we consider). The argument for correctness is the same as before.

> **Answer:** For 3: For termination we can use high - low. This interval is shrinking in each iteration and will eventually be empty. Before it is empty, though, we must have hit an interval of length 1 that contains the number we are looking for. Why? Because whenever `high - low > 2`, both `mid - low` and `high - low` >= 2 and when `high - low == 2` we have `mid = low` and either we have found the element at `mid` or the element is at `mid + 1` (since it must be in the interval) and the next recursion has an interval of length one where the element we are searching for is at the front.

**Exercise:** Would you judge all three approaches to be equally efficient in finding the right number? If not, how would you order the three strategies such that the method most likely to get the right number first is ranked highest and the algorithm most likely to get the right number last is ranked lowest. Justify your answer.

> **Answer:** In the first two strategy we eliminate one element at a time until we find the one we are searching for. In the third strategy we eliminate half the remaining interval in each iteration. We would therefore expect the third strategy to be faster than the first two.

If you do not lie to the computer when it asks you about its guess compared to the number you are thinking of, this program implements the first strategy:

```python
# The following code is just to setup the exercise.
# You do not need to understand but can jump to the game below.

def input_selection(prompt, options):
    """Get user input, restrict it to fixed options."""
    modified_prompt = "{} [{}]: ".format(
        prompt.strip(), ", ".join(options)
    )
    while True:
        inp = input(modified_prompt)
        if inp in options:
            return inp
        # nope, not a valid answer...
        print("Invalid choice! Must be in [{}]".format(
            ", ".join(options)
        ))

# Here, we implement the computer's strategy for guessing
# the number you are thinking of. Don't lie to the
# computer. It won't punish you, but it will frown upon it.
for guess in range(1, 21):
    result = input_selection(
        "I'm guessing {}\nHow is my guess?".format(guess),
        ["low", "hit", "high"]
    )
    if result == "hit":
        print("Wuhuu!")
        break
    else:
        print("I must have been too low, right?", result)
```

**Exercise:** Implement the other two strategies and test them.

> **Answer:** Counting down from 20 to 1 can be implemented like this:

```python
for guess in range(20,0,-1):
    result = input_selection(
        "How is my guess {}?".format(guess), 
        ["low", "hit", "high"]
    )
    if result == "hit":
        print("Wuhuu!")
        break
    else:
        print("I must have been too hight, right? ", result)
```

> **Answer:** Cutting the interval in half in each iteration can be implemented like this:

```python
lower_bound = 1
upper_bound = 20
while True:
    guess = (upper_bound + lower_bound) // 2
    result = input_selection(
        "How is my guess {}?".format(guess),
        ["low", "hit", "high"]
    )
    if result == "hit":
        print("Wuhuu!")
        break
    elif result == "low":
        lower_bound = guess + 1
    else:
        upper_bound = guess - 1
```


## Finding square roots

**Exercise:** From the description alone you can argue that *if* the method terminates, it will report a correct answer. Prove that the algorithm is correct.

> **Answer:** We only terminate when |S/xᵢ - xᵢ|< ε. We know that if xᵢ < S/xᵢ then xᵢ_i ≤ x < S/xᵢ, so xᵢ is within ε of the true value, x. If xᵢ > S/xᵢ we know that S/xᵢ < x ≤ xᵢ, and again we know that xᵢ is within ε\ of the true value, x.

In each iteration, we update the interval in which we know √S resides by cutting the previous interval in half.

**Exercise:** Use this to prove that the algorithm terminates.

> **Answer:** We can use |S/xᵢ - xᵢ - ε as our termination function. Each iteration decreases the |S/xᵢ - xᵢ| by one half, so the size of the interval moves asymptotically towards zero. This means that eventually it will be smaller than any ε, so the algorithm must terminate.

**Exercise:** Implement and test this algorithm.

```python
lower_bound = 0
upper_bound = S
x = upper_bound / 2
while (upper_bound - lower_bound) > ε:
    x = (lower_bound + upper_bound) / 2
    if x**2 > S:
        lower_bound = S/x
        upper_bound = x
    else:
        lower_bound = x
        upper_bound = S/x
```

You can use this as a test run:

```python
from math import sqrt

# let us compute the square root of 2 within 
# an accuracy of one in a hundred thousands
S = 2
ε = 1e-5

lower_bound = 0
upper_bound = S
x = upper_bound / 2
while (upper_bound - lower_bound) > ε:
    x = (lower_bound + upper_bound) / 2
    if x**2 > S:
        lower_bound = S/x
        upper_bound = x
    else:
        lower_bound = x
        upper_bound = S/x


print("We expect to agree on the first four decimals,")
print("since these are in ten-thousands, but not necessarily")
print("at the fifth decimal, which is below our precision.\n")
print("Results:")
print("Python suggests {:.5f}".format(sqrt(2)))
print("Babylonian method gave us {:.5f}".format(x))
```

## Changing base

My implementation looks like this:

```python
digits = {}

for i in range(0,10):
    digits[i] = str(i)

digits[10] = 'A'
digits[11] = 'B'
digits[12] = 'C'
digits[13] = 'D'
digits[14] = 'E'
digits[15] = 'F'

m = 32

b = 16
base_b = []
n = m
while n > 0:
    base_b.append(digits[n % b])
    n //= b
print(m, "in base", b, "is", "".join(base_b[::-1]))

b = 10
n = m
base_b = []
while n > 0:
    base_b.append(digits[n % b])
    n //= b
print(m, "in base", b, "is", "".join(base_b[::-1]))


b = 8
n = m
base_b = []
while n > 0:
    base_b.append(digits[n % b])
    n //= b
print(m, "in base", b, "is", "".join(base_b[::-1]))

b = 4
n = m
base_b = []
while n > 0:
    base_b.append(digits[n % b])
    n //= b
print(m, "in base", b, "is", "".join(base_b[::-1]))

b = 2
n = m
base_b = []
while n > 0:
    base_b.append(digits[n % b])
    n //= b
print(m, "in base", b, "is", "".join(base_b[::-1]))
```

## Sieve of Eratosthenes

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

Pick `n` and try it out.


## Longest increasing substring

My implementation looks like this:

```python

x = [12, 45, 32, 65, 78, 23, 35, 45, 57]
# We can always have a longest sequence containing just the first character
longest_from, longest_to, longest_len = 0, 1, 1

# Brute force solution
for i in range(len(x)):
	for j in range(i + 1, len(x)):
		if x[j] <= x[j - 1]:
			break
	if j - i > longest_len:
		longest_from, longest_to, longest_len = i, j, j - i

print(longest_from, longest_to, x[longest_from:longest_to])

# Linear time solution
longest_from, longest_to, longest_len = 0, 1, 1
current_from = 0
for i in range(1, len(x)):
	# the current interval is [current_from, i)
	if x[i - 1] >= x[i]:
		# we have to start a new interval
		current_len = i - 1 - current_from
		if current_len > longest_len:
			longest_from, longest_to, longest_len = current_from, i, current_len
		# start new interval
		current_from, current_len = i, 1

print(longest_from, longest_to, x[longest_from:longest_to])
```

## Computing power-sets

The hint tells you that there is a close correspondence between the powers of a set, S, and the binary representation of all the numbers from zero to `len(S)`.

Consider this program:

```python
n = 3
m = 2**n
for i in range(m):
	reverse_bits = [0] * n
	k = 0
	while i > 0:
		reverse_bits[k] = i % 2
		i //= 2
		k += 1
	print(reverse_bits[::-1])
```

It is a slight variation on the program from the chapter that gets the binary representation of a number. This variant always have n (binary) digits, which the algorithm in the chapter does not, but otherwise it is the same.

If you run it with n equal to three, as in the code listing above, you get the output

```
[0, 0, 0]
[0, 0, 1]
[0, 1, 0]
[0, 1, 1]
[1, 0, 0]
[1, 0, 1]
[1, 1, 0]
[1, 1, 1]
```

If you extract, from the list S, the indices where the bit is set, you get subsets of S, and if you extract the sets for each of these lists you have the power-set of S.

```python
S = ['a', 'b', 'c']
powS = []

print("powerset of", S)
n = len(S)
m = 2**n
for i in range(m):
	j = 0
	x = []
	while i > 0:
		if i % 2 == 1:
			x.append(S[j])
		i //= 2
		j += 1
	print(x)
	powS.append(x)
print()

print("powS =", powS)
```

## Longest increasing subsequence

My solution is this implementation (I explain it below):

```python
x = [12, 45, 32, 65, 78, 23, 35, 45, 57]

# best so far
best_indices = []

# Set up for computing all combination of indices
n = len(x)
m = 2**n
for i in range(m):
	# collect indices
	j = 0
	indices = []
	while i > 0:
		if i % 2 == 1:
			indices.append(j)
		i //= 2
		j += 1

	# check if indices gives us an increasing sequence
	for k in range(1, len(indices)):
		prev, this = indices[k-1], indices[k]
		if x[prev] >= x[this]:
			# not increasing, so break
			break
	else:
		# the else part of a for-loop is executed
		# when we leave it by ending the loop
		# and not when breaking...
		if len(indices) > len(best_indices):
			best_indices = indices

vals = [x[i] for i in best_indices]
print("increasing sequence:", best_indices, vals)


for i in range(m):
	# collect indices
	j = 0
	indices = []
	while i > 0:
		if i % 2 == 1:
			indices.append(j)
		i //= 2
		j += 1

	# check if indices gives us an increasing sequence
	increasing = True
	for k in range(1, len(indices)):
		prev, this = indices[k-1], indices[k]
		if x[prev] >= x[this]:
			# not increasing, so break
			increasing = False
			break
	if increasing:
		# the else part of a for-loop is executed
		# when we leave it by ending the loop
		# and not when breaking...
		if len(indices) > len(best_indices):
			best_indices = indices

vals = [x[i] for i in best_indices]
print("increasing sequence:", best_indices, vals)
```

We start by defining some variables to hold the best sequence we have seen so far.

```python
best_indices = []
```

We do not keep track of the length; we can always get that from `len(best_indices)`.

Now we take the same approach as for computing power-sets. If we get the power-set of indices using the algorithm from the previous exercise, then we get the indices in increasing order.

```python
# Set up for computing all combination of indices
n = len(x)
m = 2**n
for i in range(m):
	# collect indices
	j = 0
	indices = []
	while i > 0:
		if i % 2 == 1:
			indices.append(j)
		i //= 2
		j += 1

	# check if indices gives us an increasing sequence
	# …
```

This code iterates through all sets of increasing indices. We can examine each in turn and test that these indices give us an increasing sequence of x values. We can simply run through the list of indices and check that each one index a value in x that is larger than the previous one. If not, we break the loop.

```python
	# check if indices gives us an increasing sequence
	for k in range(1, len(indices)):
		prev, this = indices[k-1], indices[k]
		if x[prev] >= x[this]:
			# not increasing, so break
			break
```

The `break` only leaves the inner-most `for`-loop, but we actually want to leave the outermost loop—we want to move on to the next candidate list of indices.

We can use a boolean flag to help us out here. We set it to `True`, but if the candidate list of indices do not describe an increasing subsequence, then we set it to `False`. Only if it is `True` do we potentially update the best sequence.

```python
	# check if indices gives us an increasing sequence
	increasing = True
	for k in range(1, len(indices)):
		prev, this = indices[k-1], indices[k]
		if x[prev] >= x[this]:
			# not increasing, so break
			increasing = False
			break
	if increasing:
		# the else part of a for-loop is executed
		# when we leave it by ending the loop
		# and not when breaking...
		if len(indices) > len(best_indices):
			best_indices = indices
```

There is actually another way to implement this. We haven’t seen this before, but loops have an `else` part, just as `if`-statements. They just behave very differently, and the name `else` is probably more confusing than the feature it implements. A keyword such as `completed` would be a better description.

The `else` block of a loop is executed if you leave the loop by running it to completion, i.e. if you run through all the elements in a `for`-loop or until the condition in a `while`-loop is `False`. the `else` block is *not* executed if you break from a loop.

So we can implement the validation of indices and the potential update of the best sequence seen so far as this:

```python
	# check if indices gives us an increasing sequence
	for k in range(1, len(indices)):
		prev, this = indices[k-1], indices[k]
		if x[prev] >= x[this]:
			# not increasing, so break
			break
	else:
		# the else part of a for-loop is executed
		# when we leave it by ending the loop
		# and not when breaking...
		if len(indices) > len(best_indices):
			best_indices = indices
```

When you are done, you can output the indices and corresponding values like this:

```python
vals = [x[i] for i in best_indices]
print("increasing sequence:", best_indices, vals)
```

## Merging

To make the algorithm concrete, I will list it as I would implement it:

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

You can find this implementation in [merge.py](merge.py).

Now, let us prove termination and correctness…

## Termination

Termination is the easiest to handle. Let `n = len(x)` and `m = len(y)`, then the termination function is `t(i,n,j,m) = (n-i) + (m-j)`. In each iteration we either increase `i` by one or we increase `j` by one; in either case we decrease `t(i,n,j,m)` by one. 

We never actually reach zero with this termination function, we will leave the loop when *either* `i == n` or `j == m`, but *if* we reached zero, then the loop-condition would be false, so `t` works as a termination function.

## Correctness

The pre-condition for the loop is that `x` and `y` are sorted. We will use the invariant that `z` contains the elements in `x[:i]` and `y[:j]` in sorted order. NB: with this slicing notation, `i` and `j` are *not* included in the slices, so `x[i]` and `y[j]` are not yet in `z`.

If we only left the loop when `i == n` and `j == m`, then that would suffice to guarantee that `z` would end up containing the merged lists. We break when *either* of these two conditions are met, so we need the invariant to say a bit more—and this bit more also makes it easier to show that it holds true at the end of each loop-iteration.

We will require that `z` contains the elements in `x[:i]` and `y[:j]` in sorted order *and* that `z[k-1] <= min(x[i:],y[j:])`. Since `x` and `y` are sorted, this means that we can append either `x[i]` or `y[j]` to `z` (if these exist) and still have a sorted list. It also means that when `x[i:]` is empty we can extend `z` with the elements in `y[j:]` and vice versa, that when `y[j:]` is empty we can extend `z` with `x[:i]`. So, if we guarantee this invariant for the loop, we are guaranteed that when we break the loop we have sorted items from `x[:i]` and `y[:j]`, and if we append the missing elements (from either `x[i:]` or `y[j:]`) then we still have a sorted list, and this list will now contain all the elements from `x` and `y`.

To see that the invariant holds true, consider the two cases in the loop:
1. `x[i] < y[j]`: Here, we append `x[i]` to `z` and increase `i`. Since the invariant tells us that `z[k-1] <= x[i]` we get a sorted list from this, and since `x[i] <= x[i+1]` (when `i < n`, since `x` is sorted) and `x[i] < y[j]`, we have `z[k] <= min(x[i+1:],y[j:])` so we satisfy the invariant.
2. `else` (which means `x[i] >= y[j]`): The invariant tells us that we can append `y[j]` to `z` and still have a sorted list. For the new `z[k] == y[j]` we then have `z[k] <= x[i]` (from the `if`-condition) and `z[k] <= y[j+1]` (because `y` is sorted), so we satisfy the invariant once more.

