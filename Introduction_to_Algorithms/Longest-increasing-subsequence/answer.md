# Longest increasing sub-sequence

You can see my full answer in [answer.py](answer.py), but below I explain each step in it.

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
