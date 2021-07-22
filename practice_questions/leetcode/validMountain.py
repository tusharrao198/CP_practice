# Valid Mountain
def solve(arr):
    n = len(arr)
    if len(arr) < 3:
        return False
    i = 1
    while i <= len(arr) - 1 and arr[i] > arr[i - 1]:
        i += 1
        print("i = ", i)
    if i == 1 or i == len(arr):
        return False
    while i <= len(arr) - 1 and arr[i] < arr[i - 1]:
        i += 1
    if i == len(arr):
        return True
    return False


tt = int(input())
for _ in range(tt):
    # n, k = map(int, input().split())
    # res = map(int, input().split())
    res = [1, 2, 3, 4, 5, 4, 3, 2, 1]
    print(solve(res))
