
# Exercises for “Introduction to Algorithms”

## Below or above

Here's a game you can play with a friend: one of you think of a number between 1 and 20, both 1 and 20 included. The other has to figure out what that number is. He or she can guess at the number, and after guessing will be told if the guess is correct,  too high, or is too low. Unless the guess is correct, the guesser must try again until the guess *is* correct.

The game can be implemented like this:

```python
# The following code is just to setup the exercise. 
# You do not need to understand but can jump to the game below.

from numpy.random import randint
def input_integer(prompt):
    """Get an integer from the user."""
    while True:
        try:
            inp = input(prompt)
            i = int(inp)
            return i
        except:
            print(inp, "is not a valid integer.")


# Here is an implementation of the game. The computer picks
# a number and you should try to guess it.

# When picking a random number, we specify the interval
# [low,high). Since high is not included in the interval,
# we need to use 1 to 21 to get a random number in the
# interval [1,20].
n = randint(1, 21, size=1)

# Now, repeat guessing until we get the right number.
guess = input_integer("Make a guess> ")
while guess != n:
    if guess > n:
        print("Your guess is too high!")
    else:
        print("Your guess is too low!")
    guess = input_integer("Make a guess> ")
print("You got it!")
```


In this game, the computer gets to pick the number and you need to guess it.

Here are three different strategies you could use to guess the number:

1. Start with one. If it isn't the right number, it has to be too low--there are no smaller numbers the right one could be. So if it isn't one, you guess it is two. If it isn't, you have once again guessed too low, so now you try three. You continue by incrementing your guess by one until you get the right answer.
2. Alternatively, you start at 20. If the correct number is 20, great, you got it in one guess, but if it is not, your guess must be too high—it cannot possibly be too small. So you try 19 instead, and this time you work your way down until you get the right answer.
3. Tired of trying all numbers from one end to the other, you can pick this strategy: you start by guessing 10. If this is correct, you are done, if it is too high, you know the real number must be in the interval [1,9], and if the guess is too low, you know the right answer must be in the interval [11,20]—so for your next guess, you pick the middle of the interval it must be. With each new guess, you update the range where the real number can hide and choose the middle of the previous range.

**Exercise:** Prove that all three strategies terminate and with the correct answer, i.e. they are algorithms for solving this problem.

**Exercise:** Would you judge all three approaches to be equally efficient in finding the right number? If not, how would you order the three strategies such that the method most likely to get the correct number first is ranked highest, and the algorithm most likely to get the right number last is rated lowest. Justify your answer.

If you do not lie to the computer when it asks you about its guess compared to the number you are thinking of, this program implements the first strategy:

```python
# The following code is just to setup the exercise. You do not need to
# understand but can jump to the game below.


def input_selection(prompt, options):
    """Get user input, restrict it to fixed options."""
    modified_prompt = "{} [{}]: ".format(
        prompt.strip(), ", ".join(options)
    )
    while True:
        inp = input(modified_prompt)
        if inp in options:
            return inp
        # nope, not a valid answer...
        print("Invalid choice! Must be in [{}]".format(
            ", ".join(options)
        ))


# Here, we implement the computer's strategy for guessing
# the number you are thinking of. Don't lie to the
# computer. It won't punish you, but it will frown upon it.
for guess in range(1, 21):
    result = input_selection(
        "I'm guessing {}\nHow is my guess?".format(guess),
        ["low", "hit", "high"]
    )
    if result == "hit":
        print("Wuhuu!")
        break
    else:
        print("I must have been too low, right?", result)
```

**Exercise:** Implement the other two strategies and test them.

When iterating from 20 and down, for the second strategy, you should always get the result `"high"` when you ask about your guess, so you can use a `for` loop and not worry about the actual result form `input_selection`. When you implement strategy number three, however, you need to keep track of a candidate interval with a lower bound, initially 1, and an upper bound, initially 20. When you guess too high, you should lower your upper bound to the value you just guessed minus one (no need to include the guess we know is too high). When you guess to low, you must increase your lower bound to the number you just guessed plus one. In both cases, after updating the interval, you should guess for the middle point in the new range. When you compute the middle value in your interval, you can use 

```python
guess = int(upper_bound + lower_bound) / 2)
```



## Finding square roots

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

In each iteration, we update the interval in which we know √S resides by cutting the previous interval in half.

**Exercise:** Use this to prove that the algorithm terminates.

**Exercise:** Implement and test this algorithm.


## Changing base

When we write a number such as 123 we usually mean this to be in base 10, that is, we implicitly understand this to be the number 3 × 10⁰ + 2 × 10¹ + 1 × 10². Starting from the right and moving towards the left, each digit represents an increasing power of tens. The number *could* also be in octal, although then we would usually write it like 123₈. If the number were in octal, each digit would represent a power of eight, and the number should be understood as 3 × 8⁰ + 2 × 8¹ + 3 × 8².

Binary, octal and hexadecimal numbers—notation where the bases are 2, 8, and 16, respectively—are frequently used in computer science as they capture the numbers you can put in one, three and four bits. The computer works with bits, so it naturally speaks binary. For us humans, binary is a pain because it requires long sequences of ones and zeros for even relatively small numbers, and it is hard for us to readily see if we have five or six or so zeroes or ones in a row.

Using octal and hexadecimal is more comfortable for humans than binary, and you can map the digits in octal and hexadecimal to three and four-bit numbers, respectively. Modern computers are based on bytes (and multiples of bytes) where a byte is eight bits. Since a hexadecimal number is four bits, you can write any number that fits into a byte using two hexadecimal digits rather than eight binary digits. Octal numbers are less useful on modern computers, since two octal digits, six bits, are too small for a byte while three octal digits, nine bits, are too larger. Some older systems, however, were based on 12-bits numbers, and there you had four octal numbers. Now, octal numbers are merely used for historical reasons; on modern computers, hexadecimal numbers are better.

Leaving computer science, base 12, called duodecimal, has been proposed as a better choice than base 10 for doing arithmetic because 12 has more factors than 10 and this system would be simpler to do multiplication and division in. It is probably unlikely that this idea gets traction, but if it did, we would have to get used to converting old decimal numbers into duodecimal.

In this exercise, we do not want to do arithmetic in different bases but want to write a function that prints an integer in different bases.

When the base is higher than 10, we need a way to represent the digits from 10 and up. There are proposed special symbols for these, and these can be found in Unicode, but we will use letters, as is typically done for hexadecimal. We won't go above base 16 so we can use this table to map a number to a digit up to that base:

```python
digits = {}

for i in range(0,10):
    digits[i] = str(i)

digits[10] = 'A'
digits[11] = 'B'
digits[12] = 'C'
digits[13] = 'D'
digits[14] = 'E'
digits[15] = 'F'
```

To get the last digit in a number, in base `b`, we can take the division rest, the modulus, and map that using the `digits` table:

```python
digits[i % b]
```

Try it out.

You can extract the base b representation of a number by building a list of digits starting with the smallest. You can use `digits[i % b]` to get the last digit and remember that in a list. Then we need to move on to the next digit. Now, if the number we are processing is n = b⁰ × a_0 + b¹ × a₁ + b² × a₂ + … + b<sup>n</sup> a<sub>m</sub>, then a₀ is the remainder in a division by b and the digit we just extracted. Additionally, if // denotes integer division, n // b = b⁰ × a₁ + b¹ × a₂ + … b<sup>m-1</sup>a<sub>m</sub>. So, we can get the next digit by first dividing n by b and then extract the smallest digit.

If you iteratively extract the lowest digit and put it in a list and then reduce the number by dividing it by b, you should eventually have a list with all the digits, although in reverse order. If your list is named `lst`, you can reverse it using this expression `lst[::-1]`. The expression says that we want `lst` from the beginning to the end—the default values of a range when we do not provide anything—in steps of minus one.

**Exercise:** Flesh out an algorithm, based on the observations above, that can print any integer in any base b <= 16. Show that your method terminates and outputs the correct string of digits.


## Sieve of Eratosthenes

The [Sieve of Eratosthenes](https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes) is an early algorithm for computing all prime numbers less than some upper bound n. It works as follows: we start with a set of candidates for numbers that could be primes, and since we do not a priori know which numbers will be primes we start with all the natural numbers from two and up to n.

```python
candidates = list(range(2, n + 1))
```

We are going to figure out which are primes by elimination and put the primes in another list that is initially empty.

```python
primes = []
```

The trick now is to remove from the candidates the numbers we know are not primes. We will require the following loop invariants:

1. All numbers in `primes` are prime.
2. No number in `candidates` can be divided by a number in `primes`.
3. The smallest number in `candidates` is a prime.

**Exercise:** Prove that the invariants are true with the initial lists defined as above.

We will now loop as long as there are candidates left. In the loop, we take the smallest number in the `candidates` list, which by the invariant must be a prime. Call it p. We then remove all candidates that are divisible by p and then add p to `primes`.

**Exercise:** Prove that the invariants are satisfied after these steps whenever they are satisfied before the steps.

**Exercise:** Prove that this algorithm terminates and is correct, i.e., that `primes` once the algorithm terminates contain all primes less than or equal to n. Correctness does not follow directly from the invariants so you might have to extend them.

**Exercise:** Implement and test this algorithm.


## Longest increasing substring

Assume you have a list of numbers, for example

```python
x = [12, 45, 32, 65, 78, 23, 35, 45, 57]
```

**Exercise:** Design an algorithm that finds the longest sub-sequence `x[i:j]` such that consecutive numbers are increasing, i.e. `x[k] < x[k+1]` for all `k` in `range(i,j)`  (or one of the longest, if there are more than one with the same length).

*Hint:* One way to approach this is to consider the longest sequence seen so far and the longest sequence up to a given index into `x`. From this, you can formalise invariants that should get you through.

## Computing power-sets


The *powerset* P(S) of a set S is the set that contains all possible subsets of S. For example, if S={a,b,c}, then 

P(S) = {∅, {a}, {b}, {c}, {a,b}, {a,c}, {b,c}, {a,b,c} }

**Exercise:** Assume that S is represented as a list. Design an algorithm that prints out all possible subsets of S. Prove that it terminates and is correct.

*Hint:* You can solve this problem by combining the numerical base algorithm with an observation about the binary representation of a number and a subset of S. We can represent any subset of S by the indices into the list representation of S. Given the indices, just pick out the elements at those indices. One way to represent a list of indices is as a binary sequence. The indices of the bits that are 1 should be included, the indices where the bits are 0 should not. If you can generate all the binary vectors of length `n = len(S)`, then you have implicitly generated all subsets of S. You can get all these bit vectors by getting all the numbers from zero to 2ⁿ and extracting the binary representation.


## Longest increasing subsequence

Notice that this problem has a different name than "longest increasing *substring*"; it is a slightly different problem. Assume, again, that you have a list of numbers. We want to find the longest sub-sequence of increasing numbers, but this time we are not looking for consecutive indices `i:j`, but a sequence of indices i₀,i₁,…,i<sub>m</sub> such that i<sub>k</sub> < i<sub>k + 1</sub>  and x[i<sub>k</sub>] < x[i<sub>k+1</sub>].

**Exercise** Design an algorithm for computing the longest (or a longest) such sequence of indices i₀,i₁,…,i<sub>m</sub>.

*Hint:* This problem is harder than the previous one, but you can brute force it by generating *all* subsequences and checking if the invariant is satisfied. This is a *very* inefficient approach, but we need to learn a little more about algorithms before we will see a more efficient solution.

## Merging

Assume you have two sorted lists, `x` and `y`, and you want to combine them into a new sequence, `z`, that contains all the elements from `x` and all the elements from `y`, in sorted order. You can create `z` by *merging* `x` and `y` as follows: have an index, `i`, into `x` and another index, `j`, into `y`—both initially zero—and compare `x[i]` to `y[j]`. If `x[i] < y[j]`, then append `x[i]` to `z` and increment `i` by one. Otherwise, append `y[j]` to `z` and increment `j`. If either `i` reaches the length of `x` or `j` reaches the end of `y`, simply copy the remainder of the other list to `z`.

**Exercise:** Argue why this approach creates the correct `z` list and why it terminates.
