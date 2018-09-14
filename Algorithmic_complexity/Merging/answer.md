# Merging

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
