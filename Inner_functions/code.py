def add(x):
	def inner(y):
		return x + y
	return inner

def div(x):
	def inner(y):
		return y / x
	return inner


def bind2nd(op, y):
	def inner(x):
		return op(x, y)
	return inner

def map(x, f):
    return [f(y) for y in x]

def sub(x, y):
    return x - y
x = list(range(5))
y = map(x, bind2nd(sub, 13))
print(y)

def mul(x, y):
    return x * y

def curry(op):
	def inner1(x):
		def inner2(y):
			return op(x, y)
		return inner2
	return inner1

times = curry(mul)

def uncurry(f):
    def u(x, y):
        return f(x)(y)
    return u

s = curry(sub)
print(s(1)(3))
u = uncurry(s)
print(u(1,3))


def uncurry(f):
    def u(*args):
        res = f
        for a in args:
            res = res(a)
        return res
    return u



s = curry(sub)
print(s(1)(3))
u = uncurry(s)
print(u(1,3))
