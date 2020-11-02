# Hidden Markov models

## Dependency graphs

You can read the joint probability from a dependency graph by adding marginal probabilities for nodes with in-degree zero and conditional probabilities for all other nodes.

**Exercise:** Write the joint probability for this graph. 


P(X[1])P(X[3])P(X[2]|X[1],X[3])
P(X[4])P(X[5]|X[4])
P(X[6]|X[5],X[2],X[3])
P(X[7]|X[4])
P(X[8]|X[5],X[6],X[7])
P(Y[1]|X[6])
P(Y[2])P(Y[3]|Y[1],Y[2])
P(Y[4]|Y[1],Y[3])


## Binomial and multinomial distributions

If I flip a coin *n* times, with a parameter 𝜃 that tells me the probability of seeing heads, what is the probability that I see *k* heads? (For physical reasons it is close to impossible to create a loaded coin, so 𝜃 will be 1/2, but bear with me, there are many systems where you get a binary outcome and the probabilities are not 50-50). A sequence of *n* tosses, ~X=(X<sub>1</sub>,X<sub>2</sub>,…,X<sub>n</sub>)~ has probability ~∏<sub>i=1</sub> P(X<sub>i</sub>) = ∏<sub>i=1</sub> 𝜃^<sup>X<sub>1</sub></sup>(1-𝜃)<sup>1-X<sub>i</sub></sup>~ if we encode heads as 1 and tails as zero (we have probability 𝜃 for head and 1-𝜃 for tail; we can multiply the probabilities because the tosses are independent). We can simplify this to ~P(X)=𝜃<sup>k</sup>(1-𝜃)<sup>n-k</sup>~ if there were *k* heads in the sequence. That is the probability for this specific sequence, but if we want to know what the probability is for a single toss, we don’t want the order of events to matter. We want to know what the probability of seeing *k* heads in *n* tosses is, because then we can set *n* to one and we have our probability. If we want the probability of *k* heads, we must sum together all the probabilities of sequences with *k* heads. For this model, because each sequence with *k* heads and *n-k* tails has the same probability, we can simply multiply with how many sequences will have *k* out of *n* heads, which is  binom(n,k), the binomial coefficient of *n* over *k*. So given 𝜃, the probability of seeing *k* heads out of *n* tosses is ~P(k;n,𝜃)=binom(n,k)𝜃<sup>k</sup>(1-𝜃)<sup>n-k</sup>~. The *n* goes as a parameter in the probability because we fix the number of tosses to *n* and do not consider it a random variable. To find the maximum likelihood estimate for 𝜃, you must maximise ~binom(n,k)𝜃<sup>k</sup>(1-𝜃)<sup>n-k</sup>$~ with respect to 𝜃. When we consider the probability a likelihood, we have fixed both *n* and *k*, so consider them constants, take the derivative with respect to 𝜃 and set the result to zero.

**Exercise:** Show that this gives you 𝜃=*k/n* as the maximum likelihood parameter. If you see *k* heads out of *n* tails, the most likely probability for a head in a single toss is *k/n*.

**Answer**

The likelihood is proportional to 𝜃<sup>k</sup>(1-𝜃)<sup>n-k</sup>, and we do not need to worry about the constant when we maximise. We can take the logarithm, since the logarithm is maximised at the same value. The log-likelihood is proportional to (k-𝜃n)/(𝜃(1-𝜃)) (just take the log of the function). Set this to zero, to find the maximum, and we get the equation k/(𝜃(1-𝜃)) = 𝜃n/(𝜃(1-𝜃)). Multiply through with 𝜃(1-𝜃) so you have k=𝜃n, and then divide through by n. Now you have 𝜃=k/n, which is thus the maximum.


## Markov models

For a sequence of observations

X = [...]

the joint probability of a Markov model is

P(X)=pi[X[0]] * T[X[0],X[1]] * T[X[1],X[2]] * ...

**Exercise:** Write a function that computes the joint probability of a sequence, `X` given parameters `T` and `pi`.



A Markov model for sequences of sunny and cloudy days can look like this:

```python
import numpy as np

SUNNY = 0
CLOUDY = 1

start_probs = [0.1, 0.9] # it is almost always cloudy
transitions_from_SUNNY = [0.3, 0.7]
transitions_from_CLOUDY = [0.4, 0.6]
transition_probs = np.array([transitions_from_SUNNY,
                             transitions_from_CLOUDY])
print(transition_probs)

def joint_prob(X):
    result = start_probs[X[0]]
    for i in range(1, len(X)):
        from_state = X[i - 1]
        to_state = X[i]
        result *= transition_probs[from_state, to_state]
    return result

X = [SUNNY, SUNNY, CLOUDY, SUNNY]
print(joint_prob(X))
```

Arbitrarily, I have specified that you have only 10% chance of starting with a sunny day, if today is sunny then tomorrow is only sunny with 30% probability, whereas if it is cloudy you have 40%. Not realistic, I know, but it is the computations rather than the statistical accuracy you should focus on.

**Exercise:** Compute the joint probability for longer sequences. You will discover that the result gets smaller the longer the sequence—not surprisingly since we are multiplying numbers numerically smaller than one. This is a problem when computers only have a finite resolution because they store them as flouting point numbers. You can, however, compute the log of the probability instead. Implement that.

```python
from math import log
def joint_log_prob(X):
    result = log(start_probs[X[0]])
    for i in range(1, len(X)):
        from_state = X[i - 1]
        to_state = X[i]
        result += log(transition_probs[from_state, to_state])
    return result
```

The probability distribution that tells you the probability of *k* heads out of *n* tosses, ~P(k;n,𝜃)= binom(n,k)𝜃<sup>k</sup>(1-𝜃)<sup>n-k</sup>~ is called the *binomial distribution* (from the binomial coefficient). If you have more than a binary outcome, say you roll dice instead of toss coins, the mathematics is very similar, and the distribution is called a *multinomial distribution*. If you see ~n<sub>i</sub>~ outcomes of state *i*, in *n* experiments, then the maximum likelihood parameter for the probability of seeing result *i* in a single experiment is ~n<sub>i</sub>/n$~. For the starting probabilities in a Markov model, 𝜋, you have a multinomial distribution. If you see *n* runs of the Markov model, and ~n<sub>i</sub>~ of the start in state *i*, then the maximum likelihood parameter for 𝜋 has ~𝜋<sub>i</sub>=n<sub>i</sub>/n~.

At first glance, the transition probabilities look different, because we have two variables in play. The transition parameter, *T*, is not a multinomial distribution. That is because it is a set of conditional probabilities, row *k* is the conditional probability ~P(X<sub>i</sub>|X<sub>i-1</sub>=k)~. Each of the rows are multinomial distributions, and you can estimate the paramers as such. Take one row at a time, say ~T[k,-]~, then look at all the transitions out of *k*—those are the states you are conditioning on—and count how many times you move to each state. If you move from *k* to *h* ~n<sub>kh</sub>~ times, and you move out of a *k* state ~n<sub>k</sub>~ times, then ~T[k,h]=n<sub>kh</sub>/n<sub>k</sub>~.

**Exercise:** Write a program that, given a set of sequences, estimates the parameters for a Markov model.

**Answer:** Count the number of times we start in a given state plus the number of times we transition. After that, normalise.

```python
import numpy as np

# I am assuming that I have K different states
start_counts = np.zeros( K )
trans_counts = np.zeros( (K, K) )
for s in seqs:
    start_counts[s[0]] += 1
    for i in range(1, len(s)):
        trans_counts[s[i-1],s[i]] += 1

pi = start_counts / np.sum(start_counts)
row_sum = np.sum(trans_counts, axis = 1)
T = np.zeros( (K, K) )
for r in range(K):
    T[r:] = trans_counts[r,:] / row_sum[r]
```

While far from as readable, you can get a slightly faster version using some Numpy magic:

```python
T = trans_counts / np.sum(trans_counts, axis = 1, keepdims=True)
```

but this is not something I want to go further into.


## Hidden Markov models

The dependency graph for a hidden Markov model looks like this:

**Exercise:** Using the rules for extracting a joint probability from a dependency graph, write down the probability ~P(X,Z)~ from the dependency graph.

P(Z[1]) prod(i=2 to 5) P(Z[i]|Z[i-1]) prod(i=1 to 5) P(X[i]|Z[i])


**Exercise:** Implement a function that takes ~X~ and ~Z~ as input and computes ~P(X,Z)~. The numbers will get too small for even relatively short sequences, so implement a function that computes ~log P(X,Z)~ as well. Obviously, you cannot just compute ~P(X,Z)~ first and then take the logarithm—you would still get a number underflow and taking the log at the end doesn’t help you. You need to take the log of each individual term and add the these log-values together.

```python
def prob(X, Z):
    res = pi[Z[0]] * E[Z[0],X[0]]
    for i in range(1, len(X)):
        res *= T[Z[i - 1], Z[i]] * E[Z[i], X[i]]
    return res

def log_prob(X, Z):
    res = log(pi[Z[0]]) + log(E[Z[0],X[0]])
    for i in range(1, len(X)):
        res += log(T[Z[i - 1], Z[i]])
        res += log(E[Z[i], X[i]])
    return res
```


**Exercise:** Given a set of HMM runs, ~(X<sub>i</sub>,Z<sub>i</sub>)~, how do you estimate the probabilities ~E[h,k]~?

**Answer** You do the same counting as we did for the Markov model.

**Exercise:** Write a program that, given a list of ~(X,Z)~ pairs estimates the parameters for a hidden Markov model.

```python
import numpy as np

# I am assuming that I have K different states
# and that there are L different output symbols
start_counts = np.zeros( K )
trans_counts = np.zeros( (K, K) )
emit_counts  = np.zeros( (K, L) )
for Z,X in seqs:
    start_counts[Z[0]] += 1
    for i in range(1, len(Z)):
        trans_counts[Z[i-1], Z[i]] += 1
    for i in range(len(Z)):
        emit_counts[Z[i], X[i]] += 1

pi = start_counts / np.sum(start_counts)
row_sum = np.sum(trans_counts, axis = 1)
T = np.zeros( (K, K) )
for r in range(K):
    T[r:] = trans_counts[r,:] / row_sum[r]
row_sum = np.sum(trans_counts, axis = 1)
E = np.zeros( (K, L) )
for r in range(K):
    E[r:] = emit_counts[r,:] / row_sum[r]
```

**Exercise:** If you have already observed the hidden sequence, ~Z~, and you want to compute ~P(X|Z)~ (but not marginalise over it), you can also exploit the rearranged formula. Take out the part that involves observable states and multiply the probabilities there. Write down the formula for this, and write a function that computes ~P(X,Z)~ when it gets input ~X~ and ~Z~. To prevent underflow, implement the function so it gives you ~log P(X,Z)~ instead of ~P(X,Z)~.

**Answer**:

This is just computing the Z sequence as a Markov model and then multiplying it with prod_i E[Z[i],X[i]]. I trust that you can implement it.
