def dfs(grid, i, j, r, c):
    if i < 0 or i >= r or j < 0 or j >= c or grid[i][j] != "1":
        return

    grid[i][j] = "2"
    dfs(grid, i + 1, j, r, c)
    dfs(grid, i, j + 1, r, c)
    dfs(grid, i - 1, j, r, c)
    dfs(grid, i, j - 1, r, c)


def numIslands(grid):
    r = len(grid)
    c = len(grid[0])
    num = 0
    for i in range(r):
        for j in range(c):
            if grid[i][j] == "1":
                dfs(grid, i, j, r, c)
                num += 1
    return num


grid = [
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"],
]

print(numIslands(grid))
