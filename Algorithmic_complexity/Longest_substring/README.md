# Longest increasing substring

Recall the exercise from the previous chapter where you should design an algorithm that finds the longest sub-sequence `x[i:j]` such that consecutive numbers are increasing, i.e. `x[k] < x[k+1]` for all `k` in `range(i,j)`  (or one of the longest, if there are more than one with the same length).

**Exercise:** What is the time complexity of your solution?

**Exercise:** Can you construct a linear-time algorithm for solving this problem?

*Hint:* One way to approach this is to consider the longest sequence seen so far and the longest sequence up to a given index into `x`. From this, you can formalise invariants that should get you through.

