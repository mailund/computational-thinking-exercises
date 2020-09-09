
password = "accAAA12#"

# I use a dictionary here just to show you that
# we can also do that
tests = {
    'lowercase': False,
    'uppercase': False,
    'numeric': False,
    'special': False,
    'length': False
}
special_characters = '$#@'

for x in password:
    if x.islower():
        tests['lowercase'] = True
    if x.isupper():
        tests['uppercase'] = True
    if x.isnumeric():
        tests['numeric'] = True
    if x in special_characters:
        tests['special'] = True

tests['length'] = 6 <= len(password) <= 16

for test, val in tests.items():
    print('Test', test, 'is', val)

valid = True
for test in tests.values():
    valid = valid and test

if valid:
    print("The password is valid")
else:
    print("The password is invalid")
