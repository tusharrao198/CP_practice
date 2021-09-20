def solve(A, B):
    res = sum(A[:B])
    s = res
    for i in range(B):
        print("B - 1 - i = ", B - 1 - i)
        s = s - A[B - 1 - i]
        print("1. s => ", s)
        print("len(A) - 1 - i => ", len(A) - 1 - i)
        s = s + A[len(A) - 1 - i]
        print("2. s => ", s)
        res = max(res, s)
        print("res => ", res)
    return res


A = [5,-2,3,1,2]
print(solve(A, 3))
