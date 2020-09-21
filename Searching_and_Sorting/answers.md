# Searching and Sorting

## Binary search

We argued that the worst-case running time for the binary search is O(log n).

**Exercise:** What is the best-case running time, and what would the input data look like to achieve it?

The best case is obviously when the key we search for is the first we ask for, so when it is in the middle of the list. In that case the running time is O(1)

## Selection sort

**Exercise:** Give an example input where selection sort is not stable.

Consider this input. I use pairs where the first item is the key and the second item is the order of the elements in the input. That is, `(2,1)` and `(1,1)` are the first occurrences of keys `2` and `1`, respectively, and `(2,2)` is the second occurrence of key `2`.

```
(2,1), (2,2), (1,1)
```

In the first iteration we search for the smallest element, which is `(1,1)`. We then swap `(2,1)` with `(1,1)`.

```
(1,1), (2,2), (2,1)
```

We have now reversed the order of the twos. Whether the algorithm is stable or not now depends on whether we pick the first or the last item that has the smallest key. If we pick the first, then the algorithm is not stable. (If you pick the last pair with the minimal key, then the algorithm wouldn’t be stable on `(2,1), (2,2), (1,1), (1,2)`—try it out to convince yourself of this).

## Insertion sort

We argued that the worst-case running time for insertion sort was O(n²) but the best-case running time was O(n).

**Exercise:** Describe what the input data, `numbers`, should look like to actually achieve the worst- and best-case running times.


If the input is already sorted, then we never swap any items. The inner loop is always terminated at the first comparison and the body is never executed.

If the input is sorted in reverse order, then the inner loop will always run through the entire prefix of sorted items, which is the maximum number of iterations it can have.


## Insertion sort

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



## Bubble sort

**Exercise:** Since O₁ and O₂ tells us that the last j elements are already the largest numbers and are already sorted, we do not need to have the inner loop iterate through these last j elements. How would you exploit this to improve the running time of bubble sort? The worst-case behaviour will not improve, but you can change the running time to about half of the one we have above. Show that this is the case.

We can modify the code just a little bit by replacing the outer `while` loop with a `for` loop that runs from zero to the length of the input (those are the maximum number of iterations the `while` loop could run). Since we know that after iteration *j* the last *j* elements are already sorted, we can cap the inner `for`-loop at `len(x) - j`.

```python
for j in range(len(x)):
    swapped = False
    for i in range(1,len(x) - j):
        if x[i-1] > x[i]:
            x[i-1], x[i] = x[i], x[i-1]
            swapped = True
    if not swapped:
        break
```

Where the first version of bubble-sort ran through the entire list in each inner loop, taking time *n* always, the second version takes time *n* the first time it is run, *n-1* the second, *n-2* the third, and so on. This sum is n(n+1)/2, so about one half of the n² of the first version.

**Exercise:** With cocktail sort, after running the outer loop j times, both the first j and the last j elements are in their final positions. Show that this is the case.

The argument is really the same as for bubble-sort and the last j elements. After the cocktail sort has iterated from left to right in iteration j, the j largest elements are sorted and in their right position. After iterating from right to left, the smallest j elements are sorted and at the right positions.

**Exercise:** Knowing that both the first and last j elements are already in their right position can be used to iterate over fewer elements in the inner loops. Modify the algorithm to exploit this. The worst case complexity will still be O(n²), but you will make fewer comparisons. How much do you reduce the number of comparisons by?

We can modify the cocktail shaker sort the same way we did bubble sort, skip the last and the first j elements:

```python
x = x[:]
for j in range(len(x)):
    swapped = False
    for i in range(1,len(x) - j):
        if x[i-1] > x[i]:
            x[i-1], x[i] = x[i], x[i-1]
            swapped = True
				
    if not swapped:
        break

    for i in range(len(x) - j - 1, j + 1, -1):
        if x[i-1] > x[i]:
            x[i-1], x[i] = x[i], x[i-1]
            swapped = True

    if not swapped:
        break
```

With this version we reduce the interval by two in each outer loop, but we run two sweeps for each outer loop, one left-to-right and one right-to-left. Therefore, if we run the outer loop n times, the running time is 2(n + (n-2) + (n-4) + … 2) which is 2 × n(n+2)/4 = n(n+2)/2.

This worst-case running time of this algorithm is worse than the improved bubble sort.

The idea with cocktail sort is that we run the outer loop fewer times than bubble sort does. With bubble sort, we know that we get at least one item to its correct location in each outer iteration. With cocktail sort, we get at least two items to the right position. Since we terminate as soon as we see no swaps, this means that the maximum number of iterations of the outer loop in bubble sort is n, but for cocktail sort it is n/2.

Since we only have half as many iterations of the outer loop, but each iteration is twice as expensive as for bubble sort, the two cancels. The cocktail sort is actually a little worse, with n(n+2)/2 instead of n(n+1)/2.

The hope, of course, is that both algorithms get *more* than a single element to its right location in each iteration, and then that cocktail sort gets more items moved to their correct position per iteration than bubble sort does.

## Comparison sort comparison

**Exercise:** Insertion sort runs in O(n²) when the input is sorted in the reverse order, but can process sorted sequences in O(n). If we can recognise that the input is ordered in reverse, we could first reverse the sequence and then run the insertion sort. Show that we can reverse a sequence, in place, in O(n). Try to adapt insertion sort, so you first recognise consecutive runs of non-increasing elements, then reverse these before you run insertion sort on the result. Show that the worst-case running time is still O(n²), but try to compare the modified algorithm with the traditional insertion sort to see if it works better in practice.

You can reverse decreasing intervals like this:

```python
k = 0
while k < len(x) - 1:
    # locate decreasing interval
    for l in range(k + 1, len(x)):
        if x[l] >= x[l - 1]: # no longer decreasing
            break
    
    # reverse it
    i, j = k, l - 1
    while j > i:
        x[i], x[j] = x[j], x[i]
        i += 1; j -= 1

    k = l # skip past the interval we just reversed

```

I use a `while` loop for `k` because I want to update it to jump past intervals we have reversed. If we do not do this, then we run through them twice, just the second time all decreasing intervals are of length one… we might as well skip them.

I stop at `len(x) - 1` instead of `len(x)` because we do not need to reverse an interval of length one; it also guarantees that we never end up with `k == l`—this could happen if `k == len(x) - 1` because we then make `l` iterate over `range(len(x), len(x))`. This doesn’t change `l`, and if `k == len(x) - 1` it is because `l` had this value when we assigned it to `k`. We do not want that, so therefore this condition in the `while` loop.

Whether you use `>=` or `>` in the test in the inner loop is a bit arbitrary. It affects the result when you hit intervals with equal key, and I have chosen to iterate through those.

It should be fairly easy to see that the reversal runs in linear time (in the length of the interval we reverse). To see that the entire algorithm runs in linear time, observe that the outer loop segments the sequence into non-overlapping intervals that we reverse. In each iteration, we identify an interval `[k,l)` that we then reverse (in time `O(l-k)`), and then we increment `k` to `l` so the outer loop never sees this interval again.

## Bucket sort 

**Exercise:** Argue why the inner loop in

```python
result_keys, result_values = [], []
for key in range(m):
	for val in buckets[key]:
		result_keys.append(key)
		result_values.append(val)
```

only executes n times.

This is almost trivial to see. We insert `n` elements in the various buckets *in total*. We never extract more elements from the buckets than we inserted. There you are, we do not iteration through the inner loop more than `n` times. This doesn’t mean that we never test the loop condition more than once, though. We try to iterate through `buckets[key]` for each `key`—including those buckets that are empty. This is the reason that the algorithm runs in O(n + m) and not just O(n).

**Exercise:** Argue why the bucket sort actually sorts the input.

If the items are inserted into the correct buckets, i.e. the keys of the items in bucket `key` are all `key`, then the proof boils down to observing that iterate through the buckets in sorted order when we output the items.
