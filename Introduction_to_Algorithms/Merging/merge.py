
x = [1, 3, 3, 4, 6, 8]
y = [2, 2, 5, 6, 7, 12, 14, 16]

n, m = len(x), len(y)
i, j = 0, 0
z = []

while i < n and j < m:
	if x[i] < y[j]:
		z.append(x[i])
		i += 1
	else:
		z.append(y[j])
		j += 1

if i < n:
	z.extend(x[i:])
if j < m:
	z.extend(y[j:])

print('z:', z)
