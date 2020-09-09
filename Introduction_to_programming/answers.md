
## Loops

**Exercise:** Assume you have a number `n` (you can pick any and write it at the top of your program):

```python
n = 42
```

Now write a look that prints

```python
print("hello, world!")
```

`n` times. You choose if you prefer a `for`- or a `while`-loop.

**Answer:**

```python
n = 42
for _ in range(n):
    print("hello, world!")
```


**Exercise:** Let us do a `while`-loop that continues until you tell it that you want to stop. You can use the function `input()` to get user input. It lets the user write an answer on the terminal prompt, and once he or she hits enter, Python get the string. So you can ask the user if you should stop using

```python
input('Do you want to stop? ')
```

Write a `while`-loop that asks the use if you should stop in each iteration, and make it stop if the user answers `'yes'`. Remember that you can tell Python to stop iterating with the keyword `break`.

**Answer:**

```python
while True:
    print("hello, world!")
    should_I_quit = input("Should I quit? ")
    if should_I_quit == "yes":
        break
```

**Exercise:** Write a loop that runs through the numbers 1 to 10 (not 0 to 9!), and in iteration one it prints `1`, in iteration two it prints `1 2`, in iteration three it prints `1 2 3`, and so forth.

**Answer:**

```python
for i in range(1, 11):
    for j in range(1, i + 1):
        print(j, end = " ")
    print()
```

**Exercises:** Write a program to construct the following pattern, using a nested for loop.

```
* 
* * 
* * * 
* * * * 
* * * * * 
* * * * 
* * * 
* * 
*
```

**Answer:**

The nested loop solution can look like this:

```python
for i in range(1, 6):
    for j in range(i):
        print("*", end = " ")
    print()
for i in range(4, -1, -1):
    for j in range(i):
        print("*", end = " ")
    print()
```

but you can also do this:

```python
for i in range(1, 6):
    print('* ' * i)
for i in range(4, -1, -1):
    print('* ' * i)
```

## Lists

Consider the list

```python
x = [1, 2, 3, 4, 5, 6]
```

**Exercise:** Write a loop over `x` that computes the sum of the numbers in `x`. Then write code to compute the mean of the numbers in `x`.

**Answer:**

```python
s = 0
for val in x:
    s += val
print("sum:", s, "mean:", s/len(x))
```


**Exercise:** Write a loop over the list `x` that creates another list, `y`, that contains the elements in `x` but multiplied by 3.

**Answer:**

First with a loop, and then with a list comprehension:

```python
y = []
for val in x:
    y.append(3 * val)
print(y)

y = [3 * val for val in x]
print(y)
```

**Exercise:** Write a loop that creates a list, `y`, that contains all even numbers in `x` (and only the even numbers). You can check if a number is even by taking the integer division remainder with two and checking if it is zero: `n % 2 == 0`.

**Answer:**

First with a loop, and then with a list comprehension:

```python
y = []
for val in x:
    if val % 2 == 0:
        y.append(val)
print(y)

y = [val for val in x if val % 2 == 0]
print(y)
```


## Counting

We use dictionaries for tables, and you can make an empty dictionary like this:

```python
table = {}
```

**Exercise:** Write code that counts how often a character is in a string. You can iterate through a string, character by character, using

```python
for c in string:
	# process the character c
```

You can then use a table to count the characters. You can increment a count using

```python
table[c] += 1
```

but you will get an error if the character isn’t in the table. But, you can check if a character is not in the table with

```python
if c not in table:
	# handle this case
```

If you insert `c` here, you avoid the problem. Go count the characters in a string.

**Answer:**

```python
table = {}
for x in string:
    if x not in table:
        table[x] = 0
    table[x] += 1

for c, count in table.items():
    print("Character '{}' occurred {} time{}".format(
        c,
        count,
        's' if count > 1 else ''
    ))
```

## Password validation

Write program to check the validity of password input by users.

* At least 1 letter between `[a-z]` and 1 letter between `[A-Z]`. You can use the methods `x.islower()` and `x.isupper()` for this.
* At least 1 number between `[0-9]`. You can use the method `x.isnumeric()` for this.
* At least 1 character from `[$#@]`.
* Minimum length 6 characters.
* Maximum length 16 characters.

**Answer:**

```python
# I use a dictionary here just to show you that
# we can also do that
tests = {
    'lowercase': False,
    'uppercase': False,
    'numeric': False,
    'special': False,
    'length': False
}
special_characters = '$#@'

for x in password:
    if x.islower():
        tests['lowercase'] = True
    if x.isupper():
        tests['uppercase'] = True
    if x.isnumeric():
        tests['numeric'] = True
    if x in special_characters:
        tests['special'] = True

tests['length'] = 6 <= len(password) <= 16

for test, val in tests.items():
    print('Test', test, 'is', val)

valid = True
for test in tests.values():
    valid = valid and test

if valid:
    print("The password is valid")
else:
    print("The password is invalid")
```

## Hex encoding

This exercise is a little more involved. We want to create a textual representation for strings of bytes—it is something that was once necessary to send binary files over email (and might still be, but I have lost track of the various internet protocols). A byte is an 8-bit number, but we will use characters in Python strings (they are a little more complex, but for the exercise it doesn’t matter). If you have a character in Python, you can get the corresponding number using the function `ord()`. For example

```python
print(ord('a'))
```

will print 97. Which numbers correspond to which characters is not set in stone, but the characters in Python use the ASCII standard for all the letters you use in English, and quite a bit of special characters. Anyway, it doesn’t matter. What matters is that we have a mapping from characters to numbers, and we can get the number for a character using `ord()`.

You can go the other way using the function `chr()`, so

```python
print(chr(ord('a')))
```

gives you `a` back. So to translate a string of bytes into something human readable, we can go through it, get the underlying numbers out (using `ord()`) and that gives us a string that we can send with an old email program. If you want to get the original string back, you run though it and translate back with `chr()`.

Well, not that fast! If you see the string `123` do you have three, two, or one number? `1`, `2`, and `3`? or `12` and `3` ? or `1` and `23`? or `123`? For the trick to work, we need some way to delimit the characters. What people did (and might still do) is to translate the numbers into hexadecimal, which is base-16 numbers. You can encode more numbers in less space that way, and you can recognise when a number starts because it will always start with `0x`. You can get the hexadecimal string from a number using the function `hex()`.

**Exercise:**

Take a string such as

```python
x = "abcdabc"
```

and run through each character, get its number, and put the hex encoding into a list. Once you have the list, `y`, you can create the corresponding string using

```python
z = ''.join(y)
```

**Answer:**

```python
# With a loop:
y = []
for c in x:
    y.append(hex(ord(c)))
z = ''.join(y)
print(z)

# With a list comprehension
z = ''.join(hex(ord(c)) for c in x)
print(z)
```


There is no particular reason to prefer hexadecimal (except that two hex-numbers is enough to encode all bytes). You could use any textual encoding, you could use any delimiter, or you could require that all the numbers had the same number of digits. They avoided the latter because numbers that start with zero are interpreted as octal in the programming language C, which was used for most programs at the time. Anyway, this is how you would encode a string of bytes into a textual representation that wouldn’t confuse old email programs.

However, encoding is not the full story. If I send you an encoded file, you probably want to decode it again. You need the real string of bytes, and that is not what I am sending you. So, you need to go through the string and translate the numbers back—first you need to get an `int` for each hexadecimal number, and then you need to translate that number into the original character (the last step, we already know that we can do with the `chr()` function).

You can split the string of hexadecimal numbers, `z`` using 

```python
z.split('0x')
```

It gets rid of the `0x` strings and give you a list of the strings between them. Through away the first element, it is an empty string and doesn’t represent a number. You can run through this list and translate the strings into integers. You need to interpret the strings as hexadecimal (and not for example decimal), so call the function `int` with an extra argument, `base = 16`. If `n` is a string in hexadecimal, then 

```python
int(n, base = 16)
```

gives you the underlying number, that you can then give to `chr()`.

**Exercise:** Write code that takes a string of hexadecimal strings and decode it into the original string.

**Answer:**

This time only with list comprehension (but with all the intermediate values):

```python
splitted = z.split('0x')[1:] # remember to remove first element
numbers = [int(n, base = 16) for n in splitted]
characters = [chr(n) for n in numbers]
x = ''.join(characters)
print(x)
```

There are other (and smarter) encodings. Now that we have mostly moved to unicode for text representations, there are many options for simple text, and for binary files there has always been many. They are optimised for different things and for different applications, so you run into them every day, without knowing them. One day, perhaps, you will need to write your own encoders and decoders—it is quite likely if you ever need to develop your own file format—and now you have seen a very simple solution.

