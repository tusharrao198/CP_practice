class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        expected = 2*sum(list(set(nums)))
        arr_sum = sum(nums)
        return expected - arr_sum
        