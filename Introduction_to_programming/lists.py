
x = [1, 2, 3, 4, 5, 6]

s = 0
for val in x:
    s += val
print("sum:", s, "mean:", s/len(x))

y = []
for val in x:
    y.append(3 * val)
print(y)

y = [3 * val for val in x]
print(y)


y = []
for val in x:
    if val % 2 == 0:
        y.append(val)
print(y)

y = [val for val in x if val % 2 == 0]
print(y)
