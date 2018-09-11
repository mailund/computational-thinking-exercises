# Changing numerical base

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

You can extract the base b representation of a number by building a list of digits starting with the smallest. You can use `digits[i % b]` to get the last digit and remember that in a list. Then we need to move on to the next digit. Now, if the number we are processing is n = b⁰ × a_0 + b^1\times a_1 + b^2 \times a_2 + \cdots + b^m a_m$, then $a_0$ is the remainder in a division by $b$ and the digit we just extracted. Additionally, if $//$ denotes integer division, $n//b=b^0\times a_1 + b^1 \times a_2 + \cdots b^{m-1}a_m$. So, we can get the next digit by first dividing $n$ by $b$ and then extract the smallest digit.

If you iteratively extract the lowest digit and put it in a list and then reduce the number by dividing it by $b$, you should eventually have a list with all the digits, although in reverse order. If your list is named `lst`, you can reverse it using this expression `lst[::-1]`. The expression says that we want `lst` from the beginning to the end—the default values of a range when we do not provide anything—in steps of minus one.

**Exercise:** Flesh out an algorithm, based on the observations above, that can print any integer in any base $b\le 16$. Show that your method terminates and outputs the correct string of digits.

You can see my answer in [answer.py](answer.py).