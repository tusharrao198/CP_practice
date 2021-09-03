t = int(input())


def check_bool(x, zeros, val):
    for j in zeros:
        x[j] = val
    count = 0
    for kk in range(len(x)):
        count += x[kk]
        if count < 0:
            return False
    if count == 0:
        return True
    else:
        return False


def check(s):
    # ddd = {"A": 0, "B": 0, "C": 0}
    main = {"(": 1, "{": 2, "[": 3, ")": -1, "}": -2, "]": -3}
    # ddd = {"(": 0, "{": 0, "[": 0, ")": 0, "}": 0, "]": 0}
    nn = [0] * len(s)
    if s[0] == s[-1]:
        return False
    for i in range(len(s)):
        nn[i] = main[s[i]]

    count = 0
    for kk in range(len(s)):
        count += nn[kk]
        if count < 0:
            return False
    if count == 0:
        return True
    else:
        return False
