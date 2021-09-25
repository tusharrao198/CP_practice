from math import inf


def longestSubarraywithSumK(arr, n, target_sum):
    i = j = 0
    sum_ = 0
    maxlength = float("-inf")
    while j < n:
        # print(sum_, i, j)
        sum_ += arr[j]
        if sum_ < target_sum:
            j += 1

        elif sum_ == target_sum:
            maxlength = max(maxlength, j - i + 1)
            j += 1

        elif sum_ > target_sum:
            while sum_ > target_sum:
                sum_ -= arr[i]
                i += 1
            # if sum_ == target_sum:
            #     maxlength = max(maxlength, j - i + 1)
            j += 1

        # print(sum_, maxlength, i, j, j == n - 1)

    if maxlength == -inf:
        maxlength = len(arr[i:j])
    return maxlength


arr = [4, 1, 1, 1, 2, 8, 5]
n = len(arr)
target_sum = 10

print(longestSubarraywithSumK(arr, n, target_sum))
