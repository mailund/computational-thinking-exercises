def Fib(n):
    if n <= 2: return 1
    else: return Fib(n - 1) + Fib(n - 2)


def recsum(x):
    if x == []: return 0
    else: return x[0] + recsum(x[1:])

def recsum_tr(x, acc = 0):
    if x == []: return acc
    else: return recsum_tr(x[1:], acc + x[0])


def min_rec(x, i = 0, acc = None):
    if i == len(x): return acc
    acc = x[i] if acc is None else min(acc, x[i])
    return min_rec(x, i + 1, acc)

def reverse_rec(x, acc = []):
    if x == []: return acc
    return reverse_rec(x[1:], [x[0]] + acc)


digits = {}

for i in range(0,10):
    digits[i] = str(i)

digits[10] = 'A'
digits[11] = 'B'
digits[12] = 'C'
digits[13] = 'D'
digits[14] = 'E'
digits[15] = 'F'

def get_last_digit(i, b):
    return digits[i % b]

def to_base(n, b, rev_digits = None):
    # get an empty list if argument is None
    rev_digits = rev_digits or []

    if n == 0:
        if rev_digits == []: return "0"
        return "".join(reversed(rev_digits))
    else:
        rev_digits.append(digits[n % b])
        return to_base(n // b, b, rev_digits)

def bsearch(x, e, low = 0, high = len(x)):
    while True:
	    if low >= high:
		    return False
	    mid = (low + high) // 2
	    if x[mid] == e:
		    return True
	    elif x[mid] < e:
		    return bsearch(x, e, mid + 1, high)
	    else:
		    return bsearch(x, e, low, mid)

def bsearch(x, e, low = 0, high = len(x)):
    while low < high:
	    mid = (low + high) // 2
	    if x[mid] == e:
		    return True
	    elif x[mid] < e:
		    return bsearch(x, e, mid + 1, high)
	    else:
		    return bsearch(x, e, low, mid)
    return False