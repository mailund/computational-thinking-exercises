# Counting primitive operations exercises

## Exercise

Consider this way of computing the mean of a sequence of numbers:

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

### Answer

```python
accumulator = 0                      # 1
for n in numbers:                    # 5 × n + 2
	accumulator += n                 # n × 1
mean = accumulator / len(numbers)    # 3
```

so (5 + 1) × n + (1 + 2 + 3) =  6 × (n + 1).

## Exercise

Consider this alternative algorithm for computing the mean of a sequence of numbers:

```python
accumulator = 0
length = 0
for n in numbers:
	accumulator += n
	length += 1
mean = accumulator / length
```

How many operations are needed here? Is it more or less efficient than the previous algorithm?

```python
accumulator = 0                  # 1
length = 0                       # 1
for n in numbers:                # 5 × n + 2
	accumulator += n             # 1 × n
	length += 1                  # 1 × n
mean = accumulator / length      # 3
```

This implementation uses (5 + 1 + 1) × n + (1 + 1 + 2 + 3) = 7 × (n + 1). It is less efficient.
