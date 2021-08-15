# https: // www.hackerrank.com/challenges/max-array-sum/problem?h_l = interview & playlist_slugs % 5B % 5D = interview-preparation-kit & playlist_slugs % 5B % 5D = dynamic-programming

# Complete the maxSubsetSum function below.

# TC = O(n)
#approach
# https: // www.geeksforgeeks.org/maximum-sum-such-that-no-two-elements-are-adjacent/

def maxSubsetSum(arr):
    incl = 0
    excl = 0
    for i in arr:
        new_excl = max(excl, incl)
        incl = excl + i
        excl = new_excl

    return max(excl, incl)
