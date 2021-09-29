# User function Template for python3


class Solution:
    # Function to find number of bits needed to be flipped to convert A to B
    def countBitsFlip(self, a, b):
        ##Your code here
        a, b = bin(a)[2:][::-1], bin(b)[2:][::-1]
        a, b = [int(i) for i in a], [int(i) for i in b]
        la, lb = len(a), len(b)
        mn = 0
        if la > lb:
            mn = lb
        else:
            mn = la

        cnt = 0
        idx = 0
        for i in range(mn):
            if a[i] != b[i]:
                cnt += 1
            idx = i

        if mn == la:
            ss = sum(b[idx + 1 :])
        else:
            ss = sum(a[idx + 1 :])

        return cnt + ss


# {
#  Driver Code Starts
# Initial Template for Python 3


import math


def main():

    T = int(input())

    while T > 0:
        ab = [int(x) for x in input().strip().split()]
        a = ab[0]
        b = ab[1]
        ob = Solution()
        print(ob.countBitsFlip(a, b))
        T -= 1


if __name__ == "__main__":
    main()
