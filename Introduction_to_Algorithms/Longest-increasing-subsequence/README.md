# Longest increasing subsequence

Notice that this problem has a different name than "longest increasing *substring*"; it is a slightly different problem. Assume, again, that you have a list of numbers. We want to find the longest sub-sequence of increasing numbers, but this time we are not looking for consecutive indices `i:j`, but a sequence of indices i₀,i₁,…,i<sub>m</sub> such that i<sub>k</sub> < i<sub>k + 1</sub>  and $x[i<sub>k</sub>] < x[i<sub>k+1</sub>]$.

**Exercise** Design an algorithm for computing the longest (or a longest) such sequence of indices i₀,i₁,…,i<sub>m</sub>.

*Hint:* This problem is harder than the previous one, but you can brute force it by generating *all* subsequences and checking if the invariant is satisfied. This is a *very* inefficient approach, but we need to learn a little more about algorithms before we will see a more efficient solution.

