# Finding square-roots

Given a positive number `S > 0`, we want to compute its positive square root, `sqrt(S)`. We don't need our answer to be perfectly accurate. Using floating point numbers with a finite number of bits to represent the uncountable set of real numbers prevents this anyway. However, we want to be able to put an upper bound on the error we get, ε, such that we are guaranteed that for our result, `S’`, we have `|S-S’|< ε`.

One algorithm that solves this problem is known as the *Babylonian method* and is based on two observations. The first is this: for any $x>0$, if $x>\sqrt{S}$ then $S/x<\sqrt{S}$ and if $S/x>\sqrt{S}$ then $x<\sqrt{S}$, i.e., if we guess at a value for the square root of $S$ and the guess is too high, we have a lower bound on what it *could* be, and if the guess is too low, we have an upper bound on what it could be, see [@fig:babylonian-method-range].

![Bounds for where to find $\sqrt{S}$ depending on where $x$ lands.](figures/Babylonian-method-range){#fig:babylonian-method-range}

To see that this is so, consider the case where $x>\sqrt{S}$ and therefore $x^2>S$. This inequality naturally also implies that $S/x^2 < x^2/x^2$, and from this we derive $S=S\frac{x^2}{x^2}>S\frac{S}{x^2}=\left(\frac{S}{x^2}\right)^2$, i.e., $S/x<\sqrt{S}$. The other case is proven similarly.

Because of this, if we start out knowing nothing about $\sqrt{S}$, it could be anywhere between $0$ and $S$, so we can make an initial guess of some $x_0$, $0<x_0<S$. If $|S-x|<\epsilon$, then $x_0$ is an acceptable output and we are done. If not, we know that $\sqrt{S}$ lies in the interval $(x/S,x)$ (if $x^2>S$) or in the interval $(x,x/s)$ (if $x^2<S$), and we can make a new guess inside that interval.

The Babylonian method for finding square roots follows this idea and work as follows:

1. First, make a guess for $x_0$, e.g. $x_0=S/2$. Any number in $(0,S)$ will do.

2. Now, repeat the following, where we denote the guess we have at iteration $i$ by $x_i$.

    1. If $|S/x_i-x_i|<\epsilon$ report $x_i$.
    2. Otherwise, update $x_{i+1}=\frac{1}{2}\left(x_i+S/x_i\right)$.
    

The test $|S/x_i-x_i|<\epsilon$ is different than the requirement we made about the error we would accept, which was $|\sqrt{S}-x_i|<\epsilon$, but since we don't know $\sqrt{S}$ we cannot test that directly. We know, however, that $\sqrt{S}$ lies in the interval $(S/x,x)$ or the interval $(x,S/x)$, so if we make this interval smaller than $\epsilon$, we have reached at least the accuracy we want.

The update $x_{i+1}=\frac{1}{2}\left(x_i+S/x_i\right)$ picks the next guess to be the average of $x_i$ and $S/x_i$, which is also the midpoint in the interval $(S/x,x)$ (for $x>S/x$) or the interval $(x,S/x)$ (for $x<S/x$), so inside the interval we know must contain $\sqrt{S}$.

**Exercise:** From this description alone you can argue that *if* the method terminates, it will report a correct answer. Prove that the algorithm is correct.

In each iteration, we update the interval in which we know $\sqrt{S}$ resides by cutting the previous interval in half.

**Exercise:** Use this to prove that the algorithm terminates.

**Exercise:** Implement and test this algorithm.


