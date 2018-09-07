# My solutions

Here are three different strategies you could use to guess the number:
1. Start with 1. If it isn't the right number, it has to be too low--there are no smaller numbers the right one could be. So if it isn't 1, you guess it is 2. If it isn't, you have once again guessed too low, so now you try 3. You continue by incrementing your guess by one until you get the right answer.
2. Alternatively, you start at 20. If the right number is 20, great, you got it in one guess, but if it is not, your guess must be too high--it cannot possibly be too small. So you try 19 instead, and this time you work your way down until you get the right answer.
3. Tired of trying all numbers from one end to the other, you can pick this strategy: you start by guessing 10. If this is correct, you are done, if it is too high, you know the real number must be in the interval $[1,9]$, and if the guess is too low, you know the right answer must be in the interval $[11,20]$--so for your next guess, you pick the middle of the interval it must be. With each new guess, you update the interval where the real number can be hidden and pick the middle of the new interval.

**Exercise:** Prove that all three strategies terminate and with the correct answer, i.e. they are algorithms for solving this problem.

> **Answer:** For 1: If you let `i` denote the current number you are considering, then 20 - `i` is your termination function. You never skip a number, so when you will eventually see all numbers between 1 and 20 and you will be told when you saw the right one.

> **Answer:** For 2: Here you can use `i` - 1 as your termination function (minus one to make the termination function hit zero at the last number we consider). The argument for correctness is the same as before.

> **Answer:** For 3: For termination we can use high - low. This interval is shrinking in each iteration and will eventually be empty. Before it is empty, though, we must have hit an interval of length 1 that contains the number we are looking for. Why? Because whenever `high - low > 2`, both `mid - low` and `high - low` >= 2 and when `high - low == 2` we have `mid = low` and either we have found the element at `mid` or the element is at `mid + 1` (since it must be in the interval) and the next recursion has an interval of length one where the element we are searching for is at the front.

**Exercise:** Would you judge all three approaches to be equally efficient in finding the right number? If not, how would you order the three strategies such that the method most likely to get the right number first is ranked highest and the algorithm most likely to get the right number last is ranked lowest. Justify your answer.

> **Answer:** In the first two strategy we eliminate one element at a time until we find the one we are searching for. In the third strategy we eliminate half the remaining interval in each iteration. We would therefore expect the third strategy to be faster than the first two.

If you do not lie to the computer when it asks you about its guess compared to the number you are thinking of, this program implements the first strategy:

```python
for guess in range(1,21):
    result = input_selection("How is my guess {}?".format(guess), ["low", "hit", "high"])
    if result == "hit":
        print("Wuhuu!")
        break
    else:
        print("I must have been too low, right? the answer was", result)
```

You can find the implementation in [game-strategy-1.py](game-strategy-1.py)

**Exercise:** Implement the other two strategies and test them.

> **Answer:** Counting down from 20 to 1 can be implemented like this:

```python
for guess in range(20,0,-1):
    result = input_selection(
        "How is my guess {}?".format(guess), 
        ["low", "hit", "high"]
    )
    if result == "hit":
        print("Wuhuu!")
        break
    else:
        print("I must have been too hight, right? ", result)
```

You can find the implementation in [game-strategy-2.py](game-strategy-2.py)

> **Answer:** Cutting the interval in half in each iteration can be implemented like this:

```python
lower_bound = 1
upper_bound = 20
while True:
    guess = (upper_bound + lower_bound) // 2
    result = input_selection(
        "How is my guess {}?".format(guess),
        ["low", "hit", "high"]
    )
    if result == "hit":
        print("Wuhuu!")
        break
    elif result == "low":
        lower_bound = guess + 1
    else:
        upper_bound = guess - 1
```

You can find the implementation in [game-strategy-3.py](game-strategy-3.py)
