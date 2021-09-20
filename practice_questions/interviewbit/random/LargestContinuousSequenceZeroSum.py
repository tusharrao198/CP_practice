from itertools import accumulate


# def prefix_sum(arr):
#     # lst = [1, 2, 3, 4, 5, 6]
#     # return [1, 3, 6, 10, 15, 21]
#     prefix_sum = accumulate(arr)
#     return [i for i in prefix_sum]

def lszero(A):
    n = len(A)
    max_len = 0
    dd = {0: -1}
    l = -1  # start index
    r = -1
    curr_sum = 0
    for i in range(n):
        curr_sum += A[i]
        if curr_sum in dd.keys():
            if max_len <  (i - dd[curr_sum]):
                max_len = i - dd[curr_sum]
                l = dd[curr_sum] + 1
                r = i
        else:
            dd[curr_sum] = i
    if max_len:        
        return A[l: r+1]
    return []

    
tt = 1
for _ in range(tt):
    # lst = [1, 2, 3, 4, 5, 0, 0, 0, 6, 7, 8, 9, 10]
    # lst = [2, 3, 1, 2, 4, 3]
    # lst = [1, 1, 1, 1, 1, 1, 1, 1]
    lst = [1, 2, -2, 4, -4]
    lst = [1, 2, -3, 3]
    target = 0
    print(lszero(lst))
