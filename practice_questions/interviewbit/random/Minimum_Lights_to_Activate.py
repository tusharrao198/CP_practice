class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        i= 0
        min_count = 0
        while i<=len(A)-1:
            print(f"i = {i} and A[i] = {A[i]}")
            l = i - B + 1
            r = min(i + B - 1, len(A)-1)
            print(f"l = {l} and r = {r}")
            check = False
            while not check and r>0 and r>l:
                print(f"A[r] = {A[r]}")
                if A[r] == 1:
                    check = True
                    min_count+=1
                r-=1

            i = r+B+1  
            print(f"i = {i}")
            if not check:
                return -1       
        return min_count     
            

        # i = 0
        # res = 0
        # while(i <len(A)):
        #     print(f"i = {i} and A[i] = {A[i]}")
        #     j = min(i + B - 1, len(A)-1)
        #     print(f"j = {j} and i + B - 1 = {i + B - 1}")
        #     flag = False
        #     while(flag == False and j > 0 and j > i - B + 1):
        #         print(f"A[j] = {A[j]}")
        #         if(A[j] == 1):
        #             flag = True
        #             res += 1
        #         j -= 1
        #     i = j+1+B
        #     if(flag == False):
        #         return -1
        # return res


s = Solution()
arr = [ 0, 0, 1, 1, 1, 0, 0, 1]
arr = [1, 1, 0, 0, 1, 1]
# arr = [0, 0, 0, 1, 0]
print(arr)
B = 1
x = s.solve(arr, B)
print(x)



