# https: // practice.geeksforgeeks.org/problems/sort-an-array-of-0s-1s-and-2s4231/1

class Solution:
    def sort012(self, arr, n):
        # code here
        c0, c1, c2 = 0, 0, 0

        for i in arr:
            if i == 0:
                c0 += 1
            if i == 1:
                c1 += 1
            if i == 2:
                c2 += 1

        for i in range(n):
            if c0 > 0:
                arr[i] = 0
                c0 -= 1
            elif c0 == 0 and c1 > 0:
                arr[i] = 1
                c1 -= 1
            elif c1 == 0 and c1 == 0 and c2 > 0:
                arr[i] = 2
                c2 -= 1
        return arr
