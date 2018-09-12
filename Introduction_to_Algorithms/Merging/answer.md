# Merging

Assume you have two sorted lists, `x` and `y`, and you want to combine them into a new sequence, `z`, that contains all the elements from `x` and all the elements from `y`, in sorted order. You can create `z` by *merging* `x` and `y` as follows: have an index, `i`, into `x` and another index, `j`, into `y`—both initially zero—and compare `x[i]` to `y[j]`. If `x[i] < y[j]`, then append `x[i]` to `z` and increment `i` by one. Otherwise, append `y[j]` to `z` and increment `j`. If either `i` reaches the length of `x` or `j` reaches the end of `y`, simply copy the remainder of the other list to `z`.

**Exercise:** Argue why this approach creates the correct `z` list and why it terminates.

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

