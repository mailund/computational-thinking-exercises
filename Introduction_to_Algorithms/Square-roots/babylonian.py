from math import sqrt

# let us compute the square root of 2 within 
# an accuracy of one in a hundred thousands
S = 2
ε = 1e-5

lower_bound = 0
upper_bound = S
x = upper_bound / 2
while (upper_bound - lower_bound) > ε:
    x = (lower_bound + upper_bound) / 2
    if x**2 > S:
        lower_bound = S/x
        upper_bound = x
    else:
        lower_bound = x
        upper_bound = S/x


print("We expect to agree on the first four decimals,")
print("since these are in ten-thousands, but not necessarily")
print("at the fifth decimal, which is below our precision.\n")
print("Results:")
print("Python suggests {:.5f}".format(sqrt(2)))
print("Babylonian method gave us {:.5f}".format(x))
