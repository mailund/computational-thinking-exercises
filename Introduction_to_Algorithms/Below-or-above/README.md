# Below or above

Here's a game you can play with a friend: one of you think of a number between 1 and 20, both 1 and 20 included. The other has to figure out what that number is. He or she can guess at the number, and after guessing will be told if the guess is correct,  too high, or is too low. Unless the guess is correct, the guesser must try again until the guess *is* correct.

The game is implemented in [game.py](game.py). In this game, the computer gets to pick the number and you need to guess it.

Here are three different strategies you could use to guess the number:

1. Start with one. If it isn't the right number, it has to be too low--there are no smaller numbers the right one could be. So if it isn't one, you guess it is two. If it isn't, you have once again guessed too low, so now you try three. You continue by incrementing your guess by one until you get the right answer.
2. Alternatively, you start at 20. If the correct number is 20, great, you got it in one guess, but if it is not, your guess must be too high—it cannot possibly be too small. So you try 19 instead, and this time you work your way down until you get the right answer.
3. Tired of trying all numbers from one end to the other, you can pick this strategy: you start by guessing 10. If this is correct, you are done, if it is too high, you know the real number must be in the interval [1,9], and if the guess is too low, you know the right answer must be in the interval [11,20]—so for your next guess, you pick the middle of the interval it must be. With each new guess, you update the range where the real number can hide and choose the middle of the previous range.

**Exercise:** Prove that all three strategies terminate and with the correct answer, i.e. they are algorithms for solving this problem.

**Exercise:** Would you judge all three approaches to be equally efficient in finding the right number? If not, how would you order the three strategies such that the method most likely to get the correct number first is ranked highest, and the algorithm most likely to get the right number last is rated lowest. Justify your answer.

If you do not lie to the computer when it asks you about its guess compared to the number you are thinking of, this program implements the first strategy:

```python
for guess in range(1,21):
    result = input_selection(
        "How is my guess {}?".format(guess),
        ["low", "hit", "high"]
    )
    if result == "hit":
        print("Wuhuu!")
        break
    else:
        print("I must have been too low, right?", result)
```

You can find the implementation in [game-strategy-1.py](game-strategy-1.py)

**Exercise:** Implement the other two strategies and test them.

When iterating from 20 and down, for the second strategy, you should always get the result `"high"` when you ask about your guess, so you can use a `for` loop and not worry about the actual result form `input_selection`. When you implement strategy number three, however, you need to keep track of a candidate interval with a lower bound, initially 1, and an upper bound, initially 20. When you guess too high, you should lower your upper bound to the value you just guessed minus one (no need to include the guess we know is too high). When you guess to low, you must increase your lower bound to the number you just guessed plus one. In both cases, after updating the interval, you should guess for the middle point in the new range. When you compute the middle value in your interval, you can use 

```python
guess = int(upper_bound + lower_bound) / 2)
```

You can find my solutions to the exercises [here](answers.md), but do not look at them before you have tried to solve them yourself. They contain spoilers.
