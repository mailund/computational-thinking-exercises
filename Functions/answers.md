# Functions

## Simple functions

**Exercise:** Write a function that takes three numbers as arguments and return their product.

**Answer:**

```python
def prod(x, y, z):
    return x * y * z
```

**Exercise:** Change the function so it only takes one argument, get another from the global scope, and assigns to a local variable for the last value.

**Answer:**

```python
x = 1
def prod(z):
    y = 2
    return x * y * z
```

**Exercise:** Write a function that takes two lists as its input and return the longest of the two.

**Answer:**

```python

def longest(x, y):
    if len(x) > len(y):
        return x
    else:
        return y
```

**Exercise:** The distance between two points, `(x1,y1)` and `(x2,y2)` is √(|`x1-x2`|²+ |`y1-y2`|²). It follows from Pythagora’s Theorem (as you should be able to see using a small drawing). Write a function that computes the distance between two functions. You can use the function `abs()` to get the absolute difference of a number, `abs(x1-x2)`. You can use the `sqrt()` function to get the square root, but you need to import it from the `math` module first:

**Answer:**

```python
from math import sqrt
def distance(x1, x2, y1, y2):
    return sqrt((x1 - y1)**2 + (x2 - y2)**2)
```


## k-mers

A k-mer is a substring of length k of some string s. For example, the k-mers for k = 3 of

```
agtagtcg
```

are

```
agt
gta
tag
agt
gtc
tcg
```

**Exercise:** Write a function, `kmers`, which returns a list of all k-mers in a given string for a specific k:

**Answer:**

```python
def kmer(x, k):
    result = []
    for i in range(0, len(x) - k + 1):
        result.append(x[i:i+k])
    return result
```

**Exercise:** Often, we're only interested in unique k-mers. Write a function, `unique_kmers`, which only returns unique k-mers. Can you use a set to make this easier?

**Answer:**

```python
def kmer(x, k):
    result = set()
    for i in range(0, len(x) - k + 1):
        result.add(x[i:i+k])
    return list(result)
```

**Exercise:** Now try to write a function that returns a list of all k-mers paired together with the number of occurrences of that k-mer in the string. Consider it a bonus if you return the list sorted according to the number of occurrences.

**Answer:**

```python
def kmer(x, k):
    result = {}
    for i in range(0, len(x) - k + 1):
        y = x[i:i+k]
        if y not in result:
            result[y] = 0
        result[y] += 1
    result = list(result.items())
    # sort results by second component
    return result
```

You can use one of your sorting algorithms to sort the list. With Python's `sort()` method, you can write

```python
def second(x): return x[1]
kmers.sort(key = second)
print(kmers)
```

Read the documentation for `sort()` to understand what happens here.


## Exceptions

**Exercise:** A DNA string consists of A, C, G, and T letters. Write a function that counts how many times each of the letters occur in a string, but raises an exception if there is a letter that isn’t one of these four.

**Answer:**

You can rely on dictionaries key error exceptions to do this:

```python
def dna_count(x):
    x = x.upper() # so we only have to worry about uppercase
    counts = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
    for n in x:
        # This will raise an exception if n is not in counts
        counts[n] += 1
    return counts
```

or you can explicitly raise an exception:

```python
def dna_count(x):
    x = x.upper() # so we only have to worry about uppercase
    counts = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
    for n in x:
        if n not in 'ACGT':
            raise Exception()
        # This will raise an exception if n is not in counts
        counts[n] += 1
    return counts
```

----

Consider this example, which I admit is a little complicated, but I will explain it below:

```python
def raises_error(x):
	if x < 0:
		raise Exception("Negative", x)
	if x > 0:
		raise Exception("Positive", x)
	return 42

def f(x):
	return raises_error(x)

def g(x):
	try:
		print(f(x))
	except Exception as e:
		if e.args[0] == "Negative":
			print("g:", e.args[0])
			return f(0)
		else:
			raise
```

We have a function, `raise_error()`, that will raise an exception if its input is either negative or positive, but return 42 if its input is 0. The function `f()` just calls `raise_error()` and cannot handle any exceptions. So if `raises_error()` throws an exception, then `f()` will simply propagate it to its caller. Function `g()` calls `f()`, but inside a `try/except`. It will print the result of `f(x)` if `f()` returns normally, but if `f()` propagates an exception, we jump to `g()`’s `except` block. Here, we name the exception `e`, and we check if it was a “Negative” error we got. If so, we print a message and call `f(0)` and returns the value (which will be 42). If `e` is a “Positive” error, we re-raise the exception using `raise` with no argument.

Now, try running this code:

```python
try:
	print(g(-1))
	print(g(1))
except Exception as e:
	print("Outer", e.args[0])
```

The first time we call `g()`, it will get an exception from `raises_error()` through `f()`. It can handle this exception, so it prints “g: Negative” and returns `f(0)`, which is 42, and `print(g(-1))` prints 42. The second time we call `g()`, `raises_error()` raises an exception again, but this time `g()` cannot handle it, so it propagates it to the global `try/except`, where the `except` block handles the exception and prints “Outer Positive”.

**Exercise:** Go through this code carefully and make sure you understand what is happening. Make a drawing of the function calls for the two calls to `g()` and how exceptions propagate from `raises_error()`.

**Answer:** I cannot do this for you...

## Parameterised insertion sort

Consider insertion sort:

```python
def insertion_sort(x):
	for i in range(1,len(x)):
		j = i
		while j > 0 and x[j-1] > x[j]:
			x[j-1], x[j] = x[j], x[j-1]
			j -= 1
	return x
```

It sorts its input in increasing order. What if we want to sort in decreasing order as well? We can parameterise the comparison `x[j-1] > x[j]`, and get what we want:

```python
def insertion_sort(x, greater_than):
	for i in range(1,len(x)):
		j = i
		while j > 0 and greater_than(x[j-1], x[j]):
			x[j-1], x[j] = x[j], x[j-1]
			j -= 1
	return x

def greater(x, y):
	return x > y
insertion_sort(x, greater)

def smaller(x, y):
	return y > x
insertion_sort(x, smaller)
```

We use a function to compare two elements, and we use two functions for the comparison, one that says that `x` is larger than `y`, so we will sort in increasing order, and one that says that `x` is smaller than `y`, and that will sort the elements in decreasing order.

**Exercise:** Go through the code and make sure you understand why it sorts in increasing and decreasing order.

**Answer:** You are on your own here as well.

## Reduce

There is classic function called `reduce()`. It takes a list and a function as input, and then it applies the function to the first and second element in the list, take the result and applies the function to that and the third element, and so on, and once it is through all the elements, it returns the result.

```
f(x[n-1], f(x_[n-2],f(x_[n-3], ..., f(x[2], f(x[1],x[0])))...)
```

If `f()` is addition, then `reduce()` will add the first two numbers, then add the result to the next, then the next, and so on, and the result is the sum of all the numbers. If `f()` is multiplication, you get the product. There are, of course, easier ways to add and multiply the numbers in a list, but as an exercise, I would like you to implement `reduce()`.

**Exercise:** Implement the `reduce()` function and use it to compute the sum and product of a list of numbers.

**Answer**:

```python
def reduce(x, f):
    if len(x) < 2:
        raise Exception("List is too short")
    val = f(x[1], x[0])
    for i in range(2, len(x)):
        val = f(x[i], val)
    return val
```