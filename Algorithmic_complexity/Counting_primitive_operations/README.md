# Counting primitive operations exercises

**Exercise:** Consider this way of computing the mean of a sequence of numbers:

```python
accumulator = 0
for n in numbers:
	accumulator += n
mean = accumulator / len(numbers)
```

Count how many primitive operations it takes. To do it correctly you need to distinguish between updating a variable and assigning a value to a new one. Updating the accumulator `accumulator += n` usually maps to a single operation on a CPU because it involves changing the value of a number that is most likely in a register. Assigning to a new variable, as in

```python
mean = accumulator / len(numbers)
```

doesn’t update `accumulator` with a new value, rather it needs to compute a division, which is one operation (and it needs `len(numbers)` before it can do this, which is another operation), and then write the result in a new variable, which is an additional operation.

**Exercise:** Consider this alternative algorithm for computing the mean of a sequence of numbers:

```python
accumulator = 0
length = 0
for n in numbers:
	accumulator += n
	length += 1
mean = accumulator / length
```

How many operations are needed here? Is it more or less efficient than the previous algorithm?

You can see my answers in [answer.md](answer.md).
