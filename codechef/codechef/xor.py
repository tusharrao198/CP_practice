n = int(input())
for i in range(n):
    zz = int(input())
    C = list(bin(zz)[2:])
    # print(C)
    A = []
    B = []
    for k in range(len(C)):
        if k == 0 and C[0] == "1":
            A.append("1")
            B.append("0")
        if k != 0 and C[k] == "1":
            B.append("1")
            A.append("0")
        if k != 0 and C[k] == "0":
            A.append("1")
            B.append("1")
    x = int("".join(A), 2)
    y = int("".join(B), 2)
    print(x * y)
