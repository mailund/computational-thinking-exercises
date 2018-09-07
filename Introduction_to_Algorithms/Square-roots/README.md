# Finding square-roots

Given a positive number S > 0, we want to compute its positive square root, √S. We don't need our answer to be perfectly accurate. Using floating point numbers with a finite number of bits to represent the uncountable set of real numbers prevents this anyway. However, we want to be able to put an upper bound on the error we get, ε, such that we are guaranteed that for our result, S’, we have |S - S’| < ε.

One algorithm that solves this problem is known as the *Babylonian method* and is based on two observations. The first is this: for any x > 0, if x > √S then S/x < √S and if S/x > √S then x < √S, i.e., if we guess at a value for the square root of S and the guess is too high, we have a lower bound on what it *could* be, and if the guess is too low, we have an upper bound on what it could be.

To see that this is so, consider the case where x > √S and therefore x² > S. This inequality naturally also implies that S/x² < x²/x², and from this we derive S = S(x²/x²) > S(S / x²) = (S/x)², i.e., S/x < √S. The other case is proven similarly.

Because of this, if we start out knowing nothing about √S, it could be anywhere between 0 and S, so we can make an initial guess of some x₀ : 0 < x₀ < S. If |S - x₀| < ε, then x₀ is an acceptable output and we are done. If not, we know that √S lies in the interval (x/S,x) (if x² > S) or in the interval (x, x/s) (if x² < S), and we can make a new guess inside that interval.

The Babylonian method for finding square roots follows this idea and work as follows:

1. First, make a guess for x₀, e.g. x₀ = S/2. Any number in (0,S) will do.

2. Now, repeat the following, where we denote the guess we have at iteration i by xᵢ.

    1. If S/xᵢ - xᵢ| < ε report xᵢ.
    2. Otherwise, update xᵢ₊₁ = 1/2(xᵢ + S/xᵢ).
    

The test |S/xᵢ - xᵢ| < ε is different from the requirement we made about the error we would accept, which was |√S - xᵢ| < ε, but since we don't know √S we cannot test that directly. We know, however, that √S lies in the interval (S/x,x) or the interval (x,S/x), so if we make this interval smaller than ε, we have reached at least the accuracy we want.

The update xᵢ₊₁ = 1/2(xᵢ + S/xᵢ) picks the next guess to be the average of xᵢ and S/xᵢ, which is also the midpoint in the interval (S/x,x) (for x > S/x) or the interval (x,S/x) (for x < S/x), so inside the interval we know must contain √S.

**Exercise:** From this description alone you can argue that *if* the method terminates, it will report a correct answer. Prove that the algorithm is correct.

In each iteration, we update the interval in which we know `√S` resides by cutting the previous interval in half.

**Exercise:** Use this to prove that the algorithm terminates.

**Exercise:** Implement and test this algorithm.


You can see my solutions [here](answers.md).
