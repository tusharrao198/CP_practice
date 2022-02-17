
from itertools import permutations

name = list("CODGAT")

l = list(permutations(name))
for i in l:
    print("".join(i))

