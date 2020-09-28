
def reduce(x, f):
    if len(x) < 2:
        raise Exception("List is too short")
    val = f(x[1], x[0])
    for i in range(2, len(x)):
        val = f(x[i], val)
    return val

x = [1, 2, 3, 4]
import operator
print(reduce(x, operator.add), sum(x))
print(reduce(x, operator.mul))
