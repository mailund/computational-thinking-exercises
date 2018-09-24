
y = list(range(5))
x = y + y[::-1] + y + [1,54,2,3,5,2,1]
print(x)

k = 0
while k < len(x) - 1:
    # locate decreasing interval
    for l in range(k + 1, len(x)):
        if x[l] >= x[l - 1]: # no longer decreasing
            break
    
    # reverse it
    if l > k + 1:
        print(k, l, x[k:l])
    i, j = k, l - 1
    while j > i:
        x[i], x[j] = x[j], x[i]
        i += 1; j -= 1

    k = l # skip past the interval we just reversed

print(x)
