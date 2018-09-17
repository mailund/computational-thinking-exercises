# Recursion

## Fibonacci

**Exercise:** Implement a recursive function that computes the $n$’th Fibonacci number.

**Exercise:** Draw the call stack for computing the fourth Fibonacci number using the implementation you did in the previous exercise.

## List exercises

**Exercise:** To compute the sum of the elements in a list, we can obviously do this iteratively:

```python
result = 0
for e in x:
  result += e
```

Implement a recursive function that computes the sum of the elements of a list.

**Exercise:** We can find the smallest element in a non-empty list, `x`, like this:

```python
smallest = x[0]
for e in x:
	smallest = min(smallest, e)
```

Write a recursive function for finding the smallest element in a list. To avoid copying the list using slices, you will want to have the function take an index parameter as an argument.

**Exercise:** Modify your function, so it returns `None` if the list is empty. The easiest way to do this is probably to include the “smallest element seen so far” as a parameter to the function, with a default value of `None`. To compute the smallest value and still handle `None` you can use this function:

```python
def my_min(x, y):
	return y if x is None else min(x, y)
```

**Exercise:** Write a recursive function that reverses a list.

**Exercise:** Recall the exercise where you had to translate a base-10 number into some other base $b$ (where we restricted the base to be less than 16). We can get the last digit of a number $i$, in base $b$ using this function:

```python
def get_last_digit(i, b):
    return digits[i % b]
```

where we defined the `digits` list as

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

We can then reduce the problem to the second-to-last digit by dividing $i$ by $b$. Implement this idea using a recursive function.

## Tail-Recursion

**Exercise:** Rewrite your recursive function for computing the sum of a list of numbers such that it becomes tail-recursive.

**Exercise:** Rewrite your recursive function for finding the smallest element in a list to a version that is tail-recursive.

**Exercise:** Do the tail-recursion transformation for your tail-recursive summation function.

**Exercise:** Do the tail-recursion transformation for your tail-recursive “find minimum” function.

**Exercise:** Consider our recursive implementation of binary search:

```python
def bsearch(x, e, low = 0, high = len(x)):
	if low >= high:
		return False
	mid = (low + high) // 2
	if x[mid] == e:
		return True
	elif x[mid] < e:
		return bsearch(x, e, mid + 1, high)
	else:
		return bsearch(x, e, low, mid)
```

This function is tail-recursive, so use the transformation to replace it with a loop. Compare it to the iterative solution we considered before this chapter.