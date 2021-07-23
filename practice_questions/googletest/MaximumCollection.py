# to be done using segment trees

## now trying three pointers

class Solution:
    def threeSum(self, nums, val):
        nums.sort()
        ans, track = [], set()
        for i in range(len(nums) - 2):
            l, r = i + 1, len(nums) - 1
            current = nums[i]
            while l < r:
                target = current + nums[l] + nums[r]
                if target == val:
                    if str([current, nums[l], nums[r]]) not in track:
                        ans.append([current, nums[l], nums[r]])
                        track.add(str([current, nums[l], nums[r]]))
                    l += 1
                    r -= 1
                elif target > 0:
                    r -= 1
                else:
                    l += 1
        return ans


s = Solution()
arr = [3, 6, 1, 4]
x = s.threeSum(arr, 10)
print(x)