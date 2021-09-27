# https://practice.geeksforgeeks.org/problems/triplet-sum-in-array-1587115621/1


def threeNumTriplets(A, n, X):
    A.sort()
    for i in range(n - 2):
        l, r = i + 1, n - 1

        curr = A[i]
        while l < r:
            target = curr + A[l] + A[r]

            if target == X:
                return True
            elif target > X:
                r -= 1
            else:
                l += 1
    return False


n, X = 5, 10  # x is target
A = [1, 2, 4, 3, 6]
print(threeNumTriplets(A, n, X))
