# Guessing game exercises

Recall the guessing game from the previous chapter, where one player thinks a number between 1 and 20 and the other has to guess it. We had three strategies for the guesser:

1. Start with one. If it isn't the right number, it has to be too low—there are no smaller numbers the right one could be. So if it isn't one, you guess it is two. If it isn't, you have once again guessed too low, so now you try three. You continue by incrementing your guess by one until you get the right answer.
2. Alternatively, you start at 20. If the right number is 20, great, you got it in one guess, but if it is not, your guess must be too high—it cannot possibly be too small. So you try 19 instead, and this time you work your way down until you get the right answer.
3. The third strategy is this: you start by guessing ten. If this is correct, you are done, if it is too high, you know the real number must be in the range [1,9], and if the guess is too low, you know the right answer must be in the range [11,20]—so for your next guess, you pick the middle of the range it must be. With each new guess, you update the interval where the real number can be hidden and pick the middle of the new range.

**Exercise:** Identify the best- and worst-case scenarios for each strategy and derive the best-case and worst-case time usage.

You can see my answer in [answer.md](answer.md).