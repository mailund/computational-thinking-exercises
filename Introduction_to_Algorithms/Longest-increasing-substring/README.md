# Longest increasing substring

Assume you have a list of numbers, for example

```python
x = [12, 45, 32, 65, 78, 23, 35, 45, 57]
```

**Exercise:** Design an algorithm that finds the longest sub-sequence `x[i:j]` such that consecutive numbers are increasing, i.e. `x[k] < x[k+1]` for all `k` in `range(i,j)`  (or one of the longest, if there are more than one with the same length).

*Hint:* One way to approach this is to consider the longest sequence seen so far and the longest sequence up to a given index into `x`. From this, you can formalise invariants that should get you through.

You can see my solution in [answer.py](answer.py).