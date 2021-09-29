import string


def ExcelColumn(N):
    m = {k + 1: v for k, v in enumerate(string.ascii_uppercase)}
    # m = ["\0"] * 50
    m = []
    i = 0
    while N > 0:
        rem = N % 26
        if rem == 0:
            m.append("Z")
            N = (N // 26) - 1
        else:
            m.append(chr((rem - 1) + ord("A")))
            N = N // 26
    m = m[::-1]
    return "".join(m)


N = 52
print(ExcelColumn(N))
