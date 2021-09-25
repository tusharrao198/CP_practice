# Max Non Negative SubArray
def inc_sub(A):
    # print(A)
    res = []
    all_ = []
    s = 0
    for i in range(len(A)):
        if A[i] >= 0:
            s = A[i]
            all_.append(A[i])
            for j in range(i):
                # print(f"A[i - j - 1] = {A[i - j - 1]}")
                if A[i - j - 1] >= 0:
                    s += A[i - j - 1]
                    all_.append(A[i - j - 1])
                else:
                    break
            res.append(all_)
        s = 0
        all_ = []
    # print(res)
    if len(res) == 0:
        return []
    else:

        res.sort(
            key=lambda x: sum(x), reverse=True
        )  # sorting based on their sum value in desc order
        m1 = []
        max_sum = sum(res[0])
        # items of res with max sum only
        for h in range(len(res)):
            if sum(res[h]) == max_sum:
                m1.append(res[h])

        m1.sort(key=lambda y: len(y), reverse=True)  # sorted w.r.t length # O(nlogn)
        return m1[0][::-1]


A = [1, 2, 5, -7, 2, 3]
# A = [-1, -1, -1, -1, -1]
# A = [10, -1, 2, 3, -4, 100]
res = inc_sub(A)
print(res)
