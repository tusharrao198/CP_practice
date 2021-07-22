mat = []
for c in range(5):
    mat.append(list(map(int, input().split())))

a, b = [3, 3]
for i in range(5):
    for j in range(5):
        if mat[i][j] == 1:
            cr = abs(a - (i + 1))
            cc = abs(b - (j + 1))
            print(cc + cr)
            break
        else:
            continue


# a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# print(len(a))
