
n = 42
for _ in range(n):
    print("hello, world!")


while True:
    print("hello, world!")
    should_I_quit = input("Should I quit? ")
    if should_I_quit == "yes":
        break

for i in range(1, 11):
    for j in range(1, i + 1):
        print(j, end = " ")
    print()

for i in range(1, 6):
    for j in range(i):
        print("*", end = " ")
    print()
for i in range(4, -1, -1):
    for j in range(i):
        print("*", end = " ")
    print()

for i in range(1, 6):
    print('* ' * i)
for i in range(4, -1, -1):
    print('* ' * i)
