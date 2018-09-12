x = [12, 45, 32, 65, 78, 23, 35, 45, 57]

# best so far
best_indices = []

# Set up for computing all combination of indices
n = len(x)
m = 2**n
for i in range(m):
	# collect indices
	j = 0
	indices = []
	while i > 0:
		if i % 2 == 1:
			indices.append(j)
		i //= 2
		j += 1

	# check if indices gives us an increasing sequence
	for k in range(1, len(indices)):
		prev, this = indices[k-1], indices[k]
		if x[prev] >= x[this]:
			# not increasing, so break
			break
	else:
		# the else part of a for-loop is executed
		# when we leave it by ending the loop
		# and not when breaking...
		if len(indices) > len(best_indices):
			best_indices = indices

vals = [x[i] for i in best_indices]
print("increasing sequence:", best_indices, vals)


for i in range(m):
	# collect indices
	j = 0
	indices = []
	while i > 0:
		if i % 2 == 1:
			indices.append(j)
		i //= 2
		j += 1

	# check if indices gives us an increasing sequence
	increasing = True
	for k in range(1, len(indices)):
		prev, this = indices[k-1], indices[k]
		if x[prev] >= x[this]:
			# not increasing, so break
			increasing = False
			break
	if increasing:
		# the else part of a for-loop is executed
		# when we leave it by ending the loop
		# and not when breaking...
		if len(indices) > len(best_indices):
			best_indices = indices

vals = [x[i] for i in best_indices]
print("increasing sequence:", best_indices, vals)
