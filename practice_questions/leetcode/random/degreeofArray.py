from typing import List

# https://leetcode.com/problems/degree-of-an-array/submissions/


class Solution:
    # Runtime: 216 ms, faster than 94.62% of Python3 online submissions for Degree of an Array.
    def findShortestSubArray(self, nums: List[int]) -> int:
        d = {}
        n = len(nums)
        for i in range(n):
            d[nums[i]] = d.get(nums[i], 0) + 1

        max_val = max(list(d.values()))
        if max_val == 1:
            return 1
        max_ele = []
        for k, v in d.items():
            if max_val == v:
                max_ele.append(k)
        # return max_ele
        positions = []
        for max_element in max_ele:
            l = 0
            r = n - 1
            index = []
            first_found = False
            last_found = False
            while l <= r:
                # print(l, nums[l], r, nums[r])
                if nums[l] == max_element and not first_found:
                    index.append(l)
                    first_found = True
                if nums[r] == max_element and not last_found:
                    index.append(r)
                    last_found = True
                if not first_found:
                    l += 1
                if not last_found:
                    r -= 1
                if first_found and last_found:
                    break
            positions.append(index)
        positions.sort(key=lambda x: abs(x[1] - x[0]) + 1, reverse=False)
        return abs(positions[0][1] - positions[0][0]) + 1
        # return positions


s = Solution()
# arr = [1, 2, 2, 3, 1, 4, 2]
# arr = [1, 2, 2, 3, 1]
# arr = [2, 2, 1, 2, 3, 4, 2]
# arr = [1, 2, 2, 1, 2, 1, 1, 1, 1, 2, 2, 2]
arr = [4, 5, 2, 2, 3, 3, 1]
a = s.findShortestSubArray(arr)
print(a)
