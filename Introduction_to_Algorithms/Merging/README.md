# Merging

Assume you have two sorted lists, `x` and `y`, and you want to combine them into a new sequence, `z`, that contains all the elements from `x` and all the elements from `y`, in sorted order. You can create `z` by *merging* `x` and `y` as follows: have an index, `i`, into `x` and another index, `j`, into `y`—both initially zero—and compare `x[i]` to `y[j]`. If `x[i] < y[j]`, then append `x[i]` to `z` and increment `i` by one. Otherwise, append `y[j]` to `z` and increment `j`. If either `i` reaches the length of `x` or `j` reaches the end of `y`, simply copy the remainder of the other list to `z`.

**Exercise:** Argue why this approach creates the correct `z` list and why it terminates.
