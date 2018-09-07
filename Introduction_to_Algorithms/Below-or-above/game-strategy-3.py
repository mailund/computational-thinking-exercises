# Below or above game

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
