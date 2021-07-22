class Solution:
    # @param A : list of strings
    # @return an integer
    def solve(self, A):
        n = len(A)
        a = float(A[0])
        b = float(A[1])
        c = float(A[2])
        for i in range(3, n):
            if ((a+b+c) > 1 and (a+b+c) < 2):
                return 1
            elif ((a+b+c) > 2):
                if (a > b and a > c):
                    a = float(A[i])
                elif (b > a and b > c):
                    b = float(A[i])
                elif (c > a and c > b):
                    c = float(A[i])
            else:
                if (a < b and a < c):
                    a = float(A[i])
                elif (b < a and b < c):
                    b = float(A[i])
                elif (c < a and c < b):
                    c = float(A[i])
        if ((a+b+c) > 1 and (a+b+c) < 2):
            return 1
        else:
            return 0

s = Solution()
# arr = ["2.673662", "2.419159", "0.573816",
#        "2.454376", "0.403605", "2.503658", "0.806191"]

arr = ["0.297657", "0.420048", "0.053365", "0.437979", "0.375614",
       "0.264731", "0.060393", "0.197118", "0.203301", "0.128168"]

x = s.solve(arr)
print(x)




    # TLE case bcoz not O(n) solution
# def solve(self, A):
#     A = sorted([float(_) for _ in A])
#     for i in range(len(A)):
#         print("AAA = ",A[i])
#         l = i+1
#         r = len(A)- 1
#         sum_ = 0
#         while l < r:
#             # print(f"A[i] = {A[i]},  A[l] = {A[l]} , A[r] = {A[r]}")
#             # print(f"A[i] + A[l] + A[r] = {A[i] + A[l] + A[r]}")
    #             sum_ = A[i] + A[l] + A[r]
    #             if sum_ >1 and sum_ <2:
    #                 # print("FOUND")
    #                 return 1
    #             # print('SUM ', sum_)                
    #             if sum_ > 2:
    #                 r -= 1
    #             elif sum_ < 1:
    #                 l += 1
    #             else:
    #                 r-= 1
    #     return 0



