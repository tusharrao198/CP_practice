# /usr/bin/python3

# approached using backtracking recursively

# https://leetcode.com/problems/subsets-ii/   with duplicates

from typing import List


class Solution:
    def solve(self, nums, ans, cur, index, index_tracker):
        if index > len(nums):
            return
        # print(f"cur = {cur}")
        ans.append(cur[:])
        # print(f"ans = {ans}")
        for i in range(index, len(nums)):
            # print(f"i = {i} and nums[i] = {nums[i]} and index_tracker = {index_tracker}")
            if nums[i] not in cur:
                cur.append(nums[i])
                if [i, nums[i]] not in index_tracker: index_tracker.append([i, nums[i]])
                # print(f"{ans, cur, i, index_tracker}")
                self.solve(nums, ans, cur, i, index_tracker)
                x = cur.pop()
                # print(f"pop = {x}")
                index_tracker.pop()
            elif nums[i] in cur and [i, nums[i]] not in index_tracker:
                # print(f"asdf")
                cur.append(nums[i])
                index_tracker.append([i, nums[i]])
                # print(f"{ans, cur, i, index_tracker}")
                self.solve(nums, ans, cur, i, index_tracker)
                x = cur.pop()
                # print(f"pop = {x}")
                index_tracker.pop()
        return

    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = []
        cur = []
        index_tracker = []
        self.solve(nums, ans, cur, 0, index_tracker)
        final = []
        for i in ans:
            if i not in final: final.append(i)
        return final


# Approach:- used the same logic of subset without duplicates but instead added a index_tracker
# which contains num in nums with its position which keeps the value distinct and help us to 
# identify whether that location has been traversed or not.

# One problem is that it works fine when pairs are made with index 0 element at the start. But when pairs are 
# started with index 1 position duplicate pairs start to emerge.
# 
# This is fixed by removing the duplicates from the final array returned using a loop.   

s = Solution()
nums = [4, 4, 4, 1, 4]  # for eg. like this one , array to be sorted.

ans = s.subsetsWithDup(sorted(nums))
print(ans)
