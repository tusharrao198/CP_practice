import math as mt

# https://www.geeksforgeeks.org/prime-factorization-using-sieve-olog-n-multiple-queries/

# Python3 program to find prime factorization
# of a number n in O(Log n) time with
# precomputation allowed.


MAXN = 100001

# stores smallest prime factor for
# every number
spf = [0 for i in range(MAXN)]

# Calculating SPF (Smallest Prime Factor)
# for every number till MAXN.
# Time Complexity : O(nloglogn)

def sieve():
    spf[1] = 1
    for i in range(2, MAXN):
        # marking smallest prime factor
        # for every number to be itself.
        spf[i] = i

    # separately marking spf for
    # every even number as 2
    for i in range(4, MAXN, 2):
        spf[i] = 2

    for i in range(3, mt.ceil(mt.sqrt(MAXN))):

        # checking if i is prime
        if spf[i] == i:

            # marking SPF for all numbers
            # divisible by i
            for j in range(i * i, MAXN, i):

                # marking spf[j] if it is
                # not previously marked
                if spf[j] == j:
                    spf[j] = i


# A O(log n) function returning prime
# factorization by dividing by smallest
# prime factor at every step
def getFactorization(x):
    ret = list()
    while x != 1:
        ret.append(spf[x])
        x = x // spf[x]

    return ret


# Returns power of p in n!
def PowerOf_p_in_nfactorial(n, p):
    ans = 0
    temp = p
    while temp <= n:
        ans += n / temp
        temp = temp * p
    return int(ans)


n = int(input())
# precalculating Smallest Prime Factor
sieve()
# calling getFactorization function
p = getFactorization(n)

for i in p:
    print(PowerOf_p_in_nfactorial(n, i), end=" ")
