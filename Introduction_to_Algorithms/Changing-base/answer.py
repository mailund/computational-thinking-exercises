
digits = {}

for i in range(0,10):
    digits[i] = str(i)

digits[10] = 'A'
digits[11] = 'B'
digits[12] = 'C'
digits[13] = 'D'
digits[14] = 'E'
digits[15] = 'F'

m = 32

b = 16
base_b = []
n = m
while n > 0:
    base_b.append(digits[n % b])
    n //= b
print(m, "in base", b, "is", "".join(base_b[::-1]))

b = 10
n = m
base_b = []
while n > 0:
    base_b.append(digits[n % b])
    n //= b
print(m, "in base", b, "is", "".join(base_b[::-1]))


b = 8
n = m
base_b = []
while n > 0:
    base_b.append(digits[n % b])
    n //= b
print(m, "in base", b, "is", "".join(base_b[::-1]))

b = 4
n = m
base_b = []
while n > 0:
    base_b.append(digits[n % b])
    n //= b
print(m, "in base", b, "is", "".join(base_b[::-1]))

b = 2
n = m
base_b = []
while n > 0:
    base_b.append(digits[n % b])
    n //= b
print(m, "in base", b, "is", "".join(base_b[::-1]))
