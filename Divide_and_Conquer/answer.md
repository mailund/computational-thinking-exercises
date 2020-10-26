# Divide and conquer

## Missing element

> You are given a sorted array, `A`. It contains n - 1 of the numbers from 1 to n. You should find the missing number.

> You can use the property that for all numbers `i` less than the missing number you have `A[i] == i`, while for all `i` larger than the missing number you have `A[i] == i - 1`.

> Design an algorithm to solve the problem and derive its running time.

You can simply do a binary search for the first index where `A[i] == i - 1`. When you are above this index, `A[i] == i - 1` and when you are below `A[i] == i` so it is trivial to determine which half you should search in at each recursive call.

## Fast multiplication

> It is fast to add numbers on a computer, but multiplication can be slow. The simple way to multiply two numbers, a × b, is to iteratively add, e.g.

```python
res = 1
for i in range(a):
	res += b
```

> If you pick the smallest of the two numbers for the range, the complexity is O(min(alb)).

> Multiplying and dividing by two is a fast operation. It is just shifting bits. If you exploit the equations

```
	a × b = (a / 2) × 2b when a is even
	a × b = (a / 2) × 2b + b when a is odd
```

> can you derive an algorithm that multilines two numbers in O(log(min(a,b))).

You apply one of the two rules in each recursion, choosing the right one best on whether a is even or not. In each recursive call we halve `a` so we will reach recursion depth O(log n). Since we only perform constant time operations per level, this gives us an O(log n) algorithm.


## Largest area under a histogram

> Consider a histogram with splits at integers 0 to n. You want to find the largest-area rectangle in it. 

![](area-problem.png)

> The area for the interval i to j is h(j-q) where h is the shortest block in the histogram between i and j. You can find the largest rectangle by going through all pairs (i,j), find the shortest block, and compute the area. Then pick the pair with the largest area. A naive implementation of this would take O(n³). (Why?)

Iterating through all pairs, i and j, takes O(n²). Inside that loop you use O(n) to find the smallest block.

> You can construct a divide-and-conquer algorithm for solving it by observing that, the largest rectangle contained in the interval i to j (not the one that goes from i to j but the largest inside it) is found in the first half, the last half, or starting before and ending after the midpoint.

> To make the algorithm efficient, you should also observe that you can compute the largest area that cuts through an index m as follows: Compute an array that, for i < m, contains the minimal height between i and m, and that for j > m, contains the minimal height between m and j.

![](area-greedy.png)

You can easily compute this array in O(n) by scanning left/right and keeping track of the smallest height as you go along.

> If you extend the rectangle around m by moving i from m down to zero and j from m up to n, and you always extend in the direction with the largest height, you can compute the largest area that spans over m in linear time.

In each step, you get a new height from the array you pre-computed. If you accept the new height, the width of the area increases by one while the height goes to the new height value.

> Construct an algorithm for solving this problem and derive its running time.

At each recursive level, you split the interval in half. Then you recursively compute the largest area to the left and the right of the midpoint. You compute the "minimal height" arrays to the left and right of the midpoint and you compute the largest area crossing the midpoint in a merge-like manner.

The time recurrence equation is `T(n) = 2T(n/2) + O(n)` which is in `O(n log n)`.


## Skylines

> You are given a list of (2D) houses, represented as triplets `(i,h,j)` where `i` and `j` are the start and end coordinates and `h` is the height. This list is not sorted.

> You should compute the skyline of these houses, i.e. a representation of the height of the tallest house at each index `i`. You shouldn’t represent the skyline like this, but as triplets, `(i,h,j)`, where `i` and `j` are points where the height of the tallest house changes and `h` is the height in the range `i` to `j`.

![](skyline.png)

> Observe the following: 

> 1. The skyline for a single house, `(i,h,j)`, is simply the list `(0,0,i); (i,h,j); (j,0,n)`. 

> 2. If you have two skylines, you can merge them in linear time.

> Prove item 2. and use it to derive an O(n log n) divide-and-conquer algorithm for computing skyline plots.


Consider the two input lists, and let the first elements be `(i,n,j)` and `(i,m,k)` (they will start at the first index when the algorithm starts, and we will enforce that as an invariant). 

Without loss of generality, say `n >= m` (if `m > n` you can flip the lists and do the same reasoning). Then we want to remove blocks from list two that are smaller than the block we already have from list 1, so remove blocks `(i',m',k')` as long as `m' <= n` and `k' <= j`. Then we have blocks `(i,n,j)` and `(i',m',k')` and we do a case analysis. (It is helpful to draw the situations, so I urge you to do that). If we remove all the blocks, then we must have the entire input (because `k'` apparently couldn't get larger than `j`), and we are done. Output `(i,n,j)` as the last block, and be done.

Otherwise: If `m' <= n` we have removed blocks contained in `(i,n,j)` but now have a block that starts smaller but goes beyond `(i,n,j)`. Output `(i,n,j)` (after that block, the next in the first list has a different height, and so will the remaining of `(i',m',k')`. Push `(j,m',k')` back to the second list. It is the remainder of the block (or the full block if `j == i'`). We satisfy the invariant and can continue.

If `m' > n`, we output `(i,n,i')` because the output has to change height there. That leaves `(i',n,j)` of the original block. It could be empty, if `i' == j`, in which case we are done with it. In that case, the next block in the first list starts at index `i'` (because it starts at index `j` and it was not the last or we would have terminated earlier). That means that we satisfy the invariant if we also put `(i',m',k')` back in the second list. Otherwise, push `(i',n,j)` back to the first list. Do that, and go back to the beginning of the loop. 

