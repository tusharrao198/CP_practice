# https://leetcode.com/problems/container-with-most-water/submissions/

# Most water
# we need to find Maximum area
def solve(height):
    # using two pointer technique
    print(f"height = {height}")
    l = 0  # left
    r = len(height) - 1  # right
    max_area = 0
    while l < r:
        print(l, r)
        max_area = max(max_area, min(height[l], height[r]) * abs(r - l))
        if height[l] > height[r]:
            r -= 1
        else:
            l += 1
    return max_area


# tt = int(input())
tt = 1
for _ in range(tt):
    # n, k = map(int, input().split())
    # res = map(int, input().split())
    res = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    print(solve(res))
