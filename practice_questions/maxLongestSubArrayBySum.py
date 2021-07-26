
# Sliding window technique

def maxLongestSubArrayBySum(nums, target):
    l, r = 0, 0
    max_len = 0
    cur = 0

    while r < len(nums):
        # print(l, r)
        cur += nums[r]
        while l<r and cur>target:
            cur -= nums[l]
            l+=1
        if cur == target:
            max_len = max(max_len, r-l + 1)
        r+=1
    return max_len


tt = 1
for _ in range(tt):
    # lst = [1, 2, 3, 4, 5, 0, 0, 0, 6, 7, 8, 9, 10]
    # lst = [2, 3, 1, 2, 4, 3]
    lst = [1, 1, 1, 1, 1, 1, 1, 1]
    target = 7
    print(maxLongestSubArrayBySum(lst, target))
