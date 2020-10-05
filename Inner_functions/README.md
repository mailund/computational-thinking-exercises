
## Mapping functions

Consider the code:

```python
def times(x):
	def inner(y):
		return x * y
	return inner

def minus(x):
	def inner(y):
		return y - x
	return inner

times_two = times(2)
minus_13 = minus(13)
```

The `times()` and `minus()` functions take one parameter, the factor you should multiply with and the number you should subtract, and return functions that do that. Here, I defined `times_two()` and `minus_13()` using them, but of course, we don’t have to create these two functions to apply them, because we could also just do

```python
def map(x, f):
	return [f(y) for y in x]

map(x, times(2))
map(x, minus(13))
```

**Exercise:** What are the scopes when we call `map()`?

**Exercise:** Write a function for addition and division.

## Binding parameters

Now define

```python
def bind1st(op, x):
	def inner(y):
		return op(x, y)
	return inner
```

and run

```python
def times(x):
	return bind1st(mul, x)
map(x, times(2))
```

**Exercise:** Work out which functions are called when you do the `map()`, and what their enclosing environments are.

**Exercise:** Write a function `bind2nd()` that binds the second argument of a function. You should be able to use it in a call like this: `map(x, bind2nd(sub, 13))`.

## Currying

This function transforms a function with two arguments into one that gets the first parameter and then produce a new function that, when you give it a parameter, evaluates the original function.

```python
def curry(op):
	def inner1(x):
		def inner2(y):
			return op(x, y)
		return inner2
	return inner1
```

Functions that you evaluate by a series of applications, with one argument at a time, are called *curried*, thus the name.

We have three functions in play her, `curry()` that gets the operator and returns the first function, `inner1()`. In the instance of the call to `curry()`, we have the variable `op`, so when we call `inner1()`, it can find it in its enclosing scope. When we call `inner1()`, we get a function instance that knows the local variable `x`, so the function that `inner1()` returns, `inner2()`, can get it from its enclosing scope (and get `op` from its enclosing scope’s enclosing scope). When we then call `inner2()`, we have the final parameter, `y`, in its local scope, it can get the other two parameters from the enclosing scope chain, so it can compute the final value.

Using `curry()`, we can define `times()` like this:

```python
times = curry(mul)
```

**Exercise:** What happens if you evaluate `curry(mul)(2)(3)`? Explain why.

**Exercise:** Work your way through a call to `times()`, to get all the functions that are called, and their enclosing environments.

**Exercise:** Going the opposite direction, taking a chain of function calls and going back to one that takes all the arguments at once, us called *uncurrying*. Write a function take takes a curried function such as `times()` and translate it into one that takes two parameters and evaluate the chain of function calls in the curried function.

## Function composition

**Exercise:** Work out what this code does, what chain of function calls are involved when you use it, and how the scopes are connected.

```python
def compose(f, g):
	def inner(x):
		return f(g(x))
	return inner

def f(x): return 3 * x
def g(x): return x - 2
h = compose(f, g)
h(42)
```

