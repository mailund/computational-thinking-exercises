
def bubble(x):
    x = x[:] # copy

    while True:
        swapped = False
        for i in range(1,len(x)):
            if x[i-1] > x[i]:
                x[i-1], x[i] = x[i], x[i-1]
                swapped = True
        if not swapped:
            break

    return x

def bubble2(x):
    x = x[:] # copy

    for j in range(len(x)):
        swapped = False
        for i in range(1,len(x) - j):
            if x[i-1] > x[i]:
                x[i-1], x[i] = x[i], x[i-1]
                swapped = True
        if not swapped:
            break

    return x

def cocktail(x):
    x = x[:]
    while True:
        swapped = False
        for i in range(1, len(x)):
            if x[i-1] > x[i]:
                x[i-1], x[i] = x[i], x[i-1]
                swapped = True
				
        if not swapped:
            break

        for i in range(len(x)-1, 1, -1):
            if x[i-1] > x[i]:
                x[i-1], x[i] = x[i], x[i-1]
                swapped = True

        if not swapped:
            break

    return x

def cocktail2(x):
    x = x[:]
    for j in range(len(x)):
        swapped = False
        for i in range(1,len(x) - j):
            if x[i-1] > x[i]:
                x[i-1], x[i] = x[i], x[i-1]
                swapped = True
				
        if not swapped:
            break

        for i in range(len(x) - j - 1, j + 1, -1):
            if x[i-1] > x[i]:
                x[i-1], x[i] = x[i], x[i-1]
                swapped = True

        if not swapped:
            break

    return x


x = [3, 1, 5, 2, 6, 23, 7, 2, 67, 2, 723, 7,23, 4]

sort_functions = [bubble, bubble2, cocktail, cocktail2]
for sort in sort_functions:
    print(sort.__name__, ":", sort(x))
    assert sorted(x) == sort(x)
    
