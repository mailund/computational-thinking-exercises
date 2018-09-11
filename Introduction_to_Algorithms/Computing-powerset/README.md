# Compute the powerset of a set

The *powerset* $P(S)$ of a set $S$ is the set that contains all possible subsets of $S$. For example, if $S=\{a,b,c\}$, then 

$$P(S) = \{\emptyset,\{a\}, \{b\}, \{c\}, \{a,b\}, \{a,c\}, \{b,c\}, \{a,b,c\}\}$$

**Exercise:** Assume that $S$ is represented as a list. Design an algorithm that prints out all possible subsets of $S$. Prove that it terminates and is correct.

*Hint:* You can solve this problem by combining the numerical base algorithm with an observation about the binary representation of a number and a subset of $S$. We can represent any subset of $S$ by the indices into the list representation of $S$. Given the indices, just pick out the elements at those indices. One way to represent a list of indices is as a binary sequence. The indices of the bits that are 1 should be included, the indices where the bits are 0 should not. If you can generate all the binary vectors of length `k=len(S)`, then you have implicitly generated all subsets of $S$. You can get all these bit vectors by getting all the numbers from zero to $2^k$ and extracting the binary representation.

