def solve(A, B):
    l = 0
    r = len(A) - 1
    count = 0
    while l <= r:
        mid = (l + r) // 2

        if A[mid] <= B:
            l = mid + 1
            print(A[mid])
            count = mid + 1

        if A[mid] > B:
            r = mid - 1

    return count


A = [1, 2, 3, 4, 4, 5]
B = 4
print(solve(A, B))
