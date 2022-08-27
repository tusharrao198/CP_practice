

def longestIncreasingSubsequence(arr):
    n = len(arr)
    lst = [1] * n

    for i in range(1, n):
        for j in range(i):
            if arr[i] > arr[j] and lst[i] < lst[j]+1:
                lst[i] = lst[j] +1
    ans = max(lst)
    return ans

def solve(A):
    n = len(A)
    lst = [1] * n

    for i in range(1, n):
        for j in range(i):
            if A[i][1] > A[j][1] and A[i][0] > A[j][1] and lst[i] < lst[j]+1:
                lst[i] = lst[j] + 1
        print(lst)
    ans = max(lst)
    return ans

arr = [50, 3, 10, 7, 40, 80]
arr = [10, 22, 9, 33, 21, 50, 41, 60]
A = [[5, 24],[39, 60],[15, 28],[27, 40],[50, 90]]
# print(longestIncreasingSubsequence(arr))
print(solve(A))


# int Solution:: solve(vector < vector < int > > & A) {
#     int n = A.size()
#     vector < int > v

#     for (int i=0
#          i < n
#          i++){
#         v.push_back(1)
#     }

#     for (int i=0
#          i < n
#          i++){
#         for (int j=0
#              j < i
#              j++){
#             if (A[i][1] > A[j][1] & & A[i][0] > A[j][1] & & v[i] < v[j]+1)
#             v[i] = v[j] + 1
#         }
#     }
#     int max = 0
#     for (int i=0
#          i < n
#          i++) {
#         if (v[i] > max) {
#             max = v[i]
#         }
#     }

#     return max
# }
