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
