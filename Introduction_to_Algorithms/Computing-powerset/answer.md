# Computing power sets

The hint tells you that there is a close correspondence between the powers of a set, S, and the binary representation of all the numbers from zero to `len(S)`.

Consider this program:

```python
n = 3
m = 2**n
for i in range(m):
	reverse_bits = [0] * n
	k = 0
	while i > 0:
		reverse_bits[k] = i % 2
		i //= 2
		k += 1
	print(reverse_bits[::-1])
```

It is a slight variation on the program from the chapter that gets the binary representation of a number. This variant always have n (binary) digits, which the algorithm in the chapter does not, but otherwise it is the same.

If you run it with n equal to three, as in the code listing above, you get the output

```
[0, 0, 0]
[0, 0, 1]
[0, 1, 0]
[0, 1, 1]
[1, 0, 0]
[1, 0, 1]
[1, 1, 0]
[1, 1, 1]
```

If you extract, from the list S, the indices where the bit is set, you get subsets of S, and if you extract the sets for each of these lists you have the power-set of S.

```python
S = ['a', 'b', 'c']
powS = []

print("powerset of", S)
n = len(S)
m = 2**n
for i in range(m):
	j = 0
	x = []
	while i > 0:
		if i % 2 == 1:
			x.append(S[j])
		i //= 2
		j += 1
	print(x)
	powS.append(x)
print()

print("powS =", powS)
```

You can get the code to experiment with in the file [answer.py](answer.py).