
x = [12, 45, 32, 65, 78, 23, 35, 45, 57]
# We can always have a longest sequence containing just the first character
longest_from, longest_to, longest_len = 0, 1, 1

# Brute force solution
for i in range(len(x)):
	for j in range(i + 1, len(x)):
		if x[j] <= x[j - 1]:
			break
	if j - i > longest_len:
		longest_from, longest_to, longest_len = i, j, j - i

print(longest_from, longest_to, x[longest_from:longest_to])

# Linear time solution
longest_from, longest_to, longest_len = 0, 1, 1
current_from = 0
for i in range(1, len(x)):
	# the current interval is [current_from, i)
	if x[i - 1] >= x[i]:
		# we have to start a new interval
		current_len = i - 1 - current_from
		if current_len > longest_len:
			longest_from, longest_to, longest_len = current_from, i, current_len
		# start new interval
		current_from, current_len = i, 1

print(longest_from, longest_to, x[longest_from:longest_to])
