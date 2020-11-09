# Classes and data structures

## Accounts

Consider this class for bank accounts. It has a balance, and you can insert and withdraw amounts of money. A class for that could look like this:

```python
class Account(object):
	def __init__(self, initial_balance):
		self.balance = initial_balance

	def insert(self, amount):
		self.balance += amount

	def withdraw(self, amount):
		if self.balance - amount < 0:
			raise Exception("Insufficient funds")
		self.balance -= amount

	def __repr__(self):
		return "Account({})".format(self.balance)
```

There is no overdrawing here—we raise an exception if there are insufficient funds.

**Exercise:** Make objects of the `Account` type and explore what happens when you insert and withdraw.


## Logs

Here is an example of a class that can log events:

```python
from datetime import datetime

class Log(object):
	def __init__(self):
		self.log = []

	def add_entry(self, entry):
		now = datetime.now()
		self.log.append("{}: {}".format(now, entry))

	def print_entries(self):
		for entry in self.log:
			print(entry)
```

You can create an object, add entries to it (they will be tagged with the time you log them), and you can print all the entries.

**Exercise:** Write a program that adds log entries to a log, and prints the log before you finish the program.

**Exercise:** Add a method that clears the log, i.e., removes all entires.

**Exercise:** I didn’t write a `__repr__()` method this time, because there isn’t any way to reconstruct the object from a list of log entries. If you add a parameter to the constructor, perhaps with a default parameter, you could do that. Try to extend the constructor and then write a `__repr__()` method that can reconstruct a `Log` object.

## Songs

**Exercise:** Write me a class, `Song`, that I can initialise with a list of the lines in the lyrics, and where I can call a method `sing_me_a_song()` that will print the lyrics:

```python
>>> happy_bday = Song(["May god bless you, ",
...                    "Have a sunshine on you,",
...                    "Happy Birthday to you !"])
>>>
>>> happy_bday.sing_me_a_song()
May god bless you,
Have a sunshine on you,
Happy Birthday to you !
```

## Points

Imagine that we have an application where we want to work with points in 2D. We can always use tuples with two coordinates, but if we want to add methods, then a `Point` class can come in handy.

**Exercise:** Write a class that represents a point.

**Exercise:** Write appropriate `__repr__()` and `__str__()` methods.

**Exercise:** Write a function `dist(p1, p2)` that computes the distance between two points. You wrote such a function when you learned about functions, but there you used four coordinates. Redo it to work on points.

**Exercise:** Would you prefer to have a function or a method for `dist()`? Explain your choice.

**Exercise:** Assuming that addition and subtraction on points work as with vectors, you do them component wise, i.e. (x₁,y₁) + (x₂, y₂) = (x₁ +x₂, y₁ +y₂). Implement magic methods `__add__()` and `__sub__()` for these.


## Polynomials

We can implement a class for manipulating polynomials. I have implemented a version where you can evaluate a polynomial at a point, and where you can add two polynomials.

```python
import itertools
class Polynomial(object):
    def __init__(self, coefficients):
        self.coefficients = coefficients

    def __repr__(self):
        return 'Polynomial({})'.format(self.coefficients)

    def __str__(self):
        terms = []
        for pow, coef in enumerate(self.coefficients):
            terms.append("{}*x^{}".format(coef, pow))
        return ' + '.join(terms)

    def __call__(self, x):
        res = 0
        for pow, coef in enumerate(self.coefficients):
            res += coef * x**pow
        return res

    def __add__(self, other):
        coefficients_pairs = \
            itertools.zip_longest(self.coefficients,
                                  other.coefficients,
                                  fillvalue = 0)
        new_coefficients = [a + b for a,b in coefficients_pairs]
        return Polynomial(new_coefficients)
```

Try it out.

```python
poly1 = Polynomial([1, 2])
poly2 = Polynomial([0, 1, 2])
poly3 = poly1 + poly2
```

**Exercise:** Subtracting a polynomial from another is as easy as adding them. Implement this in the `__sub__()` method. Be careful that you do not modify any of the two original polynomials.

**Exercise:** Multiplying two polynomials is more complicated, but try to implement the `__mul__()` method for the class. If it is difficult, then restrict your implementation to multiplying with a constant—that is just multiplying all coefficients by the constant.


