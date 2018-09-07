# My Answers

**Exercise:** From the description alone you can argue that *if* the method terminates, it will report a correct answer. Prove that the algorithm is correct.

> **Answer:** We only terminate when |S/xᵢ - xᵢ|< ε. We know that if xᵢ < S/xᵢ then xᵢ_i ≤ x < S/xᵢ, so xᵢ is within ε of the true value, x. If xᵢ > S/xᵢ we know that S/xᵢ < x ≤ xᵢ, and again we know that xᵢ is within ε\ of the true value, x.

In each iteration, we update the interval in which we know √S resides by cutting the previous interval in half.

**Exercise:** Use this to prove that the algorithm terminates.

> **Answer:** We can use |S/xᵢ - xᵢ - ε as our termination function. Each iteration decreases the |S/xᵢ - xᵢ| by one half, so the size of the interval moves asymptotically towards zero. This means that eventually it will be smaller than any ε, so the algorithm must terminate.

**Exercise:** Implement and test this algorithm.

```python
lower_bound = 0
upper_bound = S
x = upper_bound / 2
while (upper_bound - lower_bound) > ε:
    x = (lower_bound + upper_bound) / 2
    if x**2 > S:
        lower_bound = S/x
        upper_bound = x
    else:
        lower_bound = x
        upper_bound = S/x
```

