
def kmer(x, k):
    result = {}
    for i in range(0, len(x) - k + 1):
        y = x[i:i+k]
        if y not in result:
            result[y] = 0
        result[y] += 1
    result = list(result.items())
    # sort results by second component
    return result

x = "agtagtcgtcgtcg"
kmers = kmer(x, 3)
print(kmers)

def second(x): return x[1]
kmers.sort(key = second)
print(kmers)
