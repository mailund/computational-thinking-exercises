import itertools

def add_coefs(coefs1, coefs2):
    return [
        a + b for a,b in
        itertools.zip_longest(coefs1, coefs2, fillvalue = 0)
    ]

def mult_scalar(scalar, coefs):
    return [scalar * coef for coef in coefs]

def shift(coefs, degree):
    return [0] * degree + coefs


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

    def __sub__(self, other):
        coefficients_pairs = \
            itertools.zip_longest(self.coefficients,
                                  other.coefficients,
                                  fillvalue = 0)
        new_coefficients = [a - b for a,b in coefficients_pairs]
        return Polynomial(new_coefficients)

    def __mul__(self, other):
        res = []
        for deg, coef in enumerate(other.coefficients):
            res = add_coefs(
                res,
                shift(
                    mult_scalar(coef, self.coefficients),
                    deg
                )
            )
        return Polynomial(res)

p1 = Polynomial([1, 2, 3])
p2 = Polynomial([2, 1])
print(p1 * p2)
