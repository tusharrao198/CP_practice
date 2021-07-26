def rotateMatrix(mat):
    for r in range(len(mat)):
        for c in range(r, len(mat[r])):
            temp = mat[r][c]
            mat[r][c] = mat[c][r]
            mat[c][r] = temp

    for r in range(len(mat)):
        for c in range(len(mat[r])//2):
            temp = mat[r][c]
            mat[r][c] = mat[r][len(mat[r]) - 1 - c]
            mat[r][len(mat[r]) - 1 - c] = temp
    return mat


# tt = int(input())
tt = 1
for _ in range(tt):
    # lst1 = list(map(int, input().split()))
    # lst2 = list(map(int, input().split()))
    lst = [[1, 2, 3], [4,5,6], [7,8,9]]
    print(rotateMatrix(lst))