# Kadane's Algorithm
def maxSumSubarray(nums):
    # base case
    if len(nums) == 1:
        return nums[0]
    if len(nums) == 2:
        return max(nums[0], nums[1], nums[0] + nums[1])

    cur = float("-inf")  # current val
    max_ = float("-inf")
    for i in range(len(nums)):
        # print(nums[i], i, cur, max_)
        if i == 0:
            cur = nums[i]
        else:
            if nums[i] > cur+nums[i]:
                cur = nums[i]
            else:
                cur += nums[i]
        max_ = max(max_, cur)
    return max_


def maxSumSubarray1(nums):
    # base case
    if len(nums) == 1:
        return nums[0]
    if len(nums) == 2:
        return max(nums[0], nums[1], nums[0] + nums[1])

    max_, cur = float("-inf"), nums[0]
    for i in range(1, len(nums)):
        cur = max(cur + nums[i], nums[i])
        max_ = max(max_, cur)
    return max_


# Time Complexity: O(n)
tt = 1
for _ in range(tt):
    lst = [-1, -2]
    print(maxSumSubarray1(lst))

