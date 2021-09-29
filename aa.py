class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer

    def findBitonicNode(self, A, B):
        n = len(A) - 1
        l, r = 0, n-1

        while l <= r:
            mid = l + (r-l)//2

            if mid-1 >= 0 and mid+1 <= n-1 and (A[mid-1] < A[mid] > A[mid+1]):
                return mid

            if A[mid] > B:
                r -= 1
            else:
                l += 1
        return -1

    def searchMain(self, arr, target):  # simple binary search
        n = len(arr)
        l, r = 0, n - 1

        while l <= r:

            mid = l + (r - l) // 2

            if arr[mid] == target:
                return mid

            elif arr[mid] > target:
                r = mid - 1

            else:
                l = mid + 1

        return -1

    def searchMainReverse(self, arr, target):  # simple binary search
        n = len(arr)
        l, r = 0, n - 1

        while l <= r:
            mid = l + (r - l) // 2

            if arr[mid] == target:
                return mid

            elif arr[mid] > target:
                l = mid + 1

            else:
                r = mid - 1

        return -1
    
    def solve(self, A, B):
        node_pos = self.findBitonicNode(A, B)
        left = self.searchMain(arr[:node_pos], B)
        right = self.searchMainReverse(arr[node_pos:], B)
        
        if left!=-1 and right!=-1:
            return left, node_pos+right


s = Solution()
arr = [3, 9, 10, 20, 17, 5, 1]
x = 20
x = s.solve(arr, x)
print(x)
