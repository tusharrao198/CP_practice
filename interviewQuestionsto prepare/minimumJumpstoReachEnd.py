# Find Minimum
# number of jumps to reach end

# O(n) approach
def miniJumps(arr, n):
    if n <= 1:
        return 0
    if arr[0] == 0:
        return -1

    jumps = 1  # number of jumps
    step = arr[0]  # total steps we can still move
    maxReach = arr[0]

    for i in range(1, n):
        if i == n - 1:
            return jumps

        maxReach = max(maxReach, i + arr[i])

        step -= 1  # using step to get to the current index

        if step == 0:
            jumps += 1

            # Check if the current index / position or lesser index
            # is the maximum reach point from the previous indexes
            if i >= maxReach:
                return -1

            # re-initialize the steps to the amount
            # of steps to reach maxReach from position i.
            step = maxReach - i
    return -1


# -----------------------------------------------------------------------------------
# Returns minimum number of jumps
# to reach arr[n-1] from arr[0]
def minJumps1(arr, n):
    jumps = [0 for i in range(n)]

    if (n == 0) or (arr[0] == 0):
        return float("inf")

    jumps[0] = 0

    # Find the minimum number of
    # jumps to reach arr[i] from
    # arr[0] and assign this
    # value to jumps[i]
    for i in range(1, n):
        jumps[i] = float("inf")
        for j in range(i):
            # print(i, j, arr[j], jumps[i], jumps[j])
            if (i <= j + arr[j]) and (jumps[j] != float("inf")):
                # print("A", i, j, arr[j], jumps[i], jumps[j])
                jumps[i] = min(jumps[i], jumps[j] + 1)
                break
    # return jumps
    return jumps[n - 1]


# arr = [1, 3, 6, 1, 0, 9]
arr = [1, 3, 5, 8, 9, 2, 6, 7, 8, 9]
size = len(arr)
print("Minimum number of jumps to reach", "end is", miniJumps(arr, size))
