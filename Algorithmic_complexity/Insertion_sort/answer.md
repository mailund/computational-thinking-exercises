# Insertion sort

Consider the insertion sort algorithm. We argued that the worst-case running time was O(n²) but the best-case running time was O(n).

**Exercise:** Describe what the input data, `numbers`, should look like to actually achieve the worst- and best-case running times.

**Answer:** 

Recall that the algorithm looks like this:

```python
for i in range(1,len(x)):
	j = i
	while j > 0 and x[j-1] > x[j]:
		x[j-1], x[j] = x[j], x[j-1]
		j -= 1		
```

For each index `i` we move the element there down until we find its place in the sorted part of `x`.

If `x` is sorted from the start, we never move an element down—we just discover that it is already where it should be. In that case, we get the linear running time.

If the elements are sorted but in the reverse order, however, each new value will be moved through all the sorted elements. In that case, we get the quadratic running time.
