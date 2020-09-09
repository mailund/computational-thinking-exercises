
string = "foobarbaz"

table = {}
for x in string:
    if x not in table:
        table[x] = 0
    table[x] += 1

for c, count in table.items():
    print("Character '{}' occurred {} time{}".format(
        c,
        count,
        's' if count > 1 else ''
    ))
