
# http://www.geeksforgeeks.org/sort-array-wave-form-2/

def sortArrayWaveform1(arr):  # O(nlogn)
    n = len(arr)
    arr.sort()
    for i in range(n-1, 2):
        arr[i], arr[i+1] = arr[i+1],  arr[i]
    return arr


def sortArrayWaveform(nums):
    n = len(nums)
    for i in range(0, n-1, 2):

        if nums[i] < nums[i+1]:
            nums[i], nums[i+1] = nums[i+1],  nums[i]

        if i!=0 and nums[i] < nums[i-1]:
            nums[i], nums[i-1] = nums[i-1],  nums[i]
    return nums


arr = [10, 90, 49, 2, 1, 5, 23]
print(sortArrayWaveform(arr))

