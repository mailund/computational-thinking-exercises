
x = "abcabc"

# With a loop:
y = []
for c in x:
    y.append(hex(ord(c)))
z = ''.join(y)
print(z)

# With a list comprehension
z = ''.join(hex(ord(c)) for c in x)
print(z)


splitted = z.split('0x')[1:] # remember to remove first element
numbers = [int(n, base = 16) for n in splitted]
characters = [chr(n) for n in numbers]
x = ''.join(characters)
print(x)
