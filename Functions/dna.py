
def dna_count(x):
    x = x.upper() # so we only have to worry about uppercase
    counts = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
    for n in x:
        if n not in 'ACGT':
            raise Exception()
        # This will raise an exception if n is not in counts
        counts[n] += 1
    return counts

x = "accgACTGGGTCAaaa"
counts = dna_count(x)
print(counts)
