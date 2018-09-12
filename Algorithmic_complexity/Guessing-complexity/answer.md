# Guessing game complexity

**Exercise:** Identify the best- and worst-case scenarios for each strategy and derive the best-case and worst-case time usage.

For the first strategy, the best case is when 1 is the value we are looking for and the worst case is when it is 20. The best-case and worst-case running times are O(1) and O(n).

For the second strategy, the best case is when we are looking for 20 and the worst case is when we are looking for 1. The best- and worst-case running times are O(1) and O(n).

For the third strategy, the best case is if we are looking for 10 (the first mid-point). In that case the running time is O(1). The worst case is when the value we are searching for is not the mid-point until there is only one element left. There are many ways that this can happen, but in all case we find the value in time O(log n), which is the worst-case complexity. We get this running time because we remove half of the range in each iteration, and if we remove half the elements in each iteration we cannot have more than log₂ n iterations before there is only one element left.

