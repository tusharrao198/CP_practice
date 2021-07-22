from sys import stdin, stdout
def fastIO():
    # n = stdin.readline()
    # stdout.write(str(n))
    arr = [int(x) for x in stdin.readline().split()]
    stdout.write(" ".join(map(str, arr)))
print(fastIO())


# for matrices without spaces
# import sys
# rd = sys.stdin.readline
# t = int(rd())
# for _ in range(t):
#     n = int(rd())
#     a = [list(list(rd().strip())) for _ in range(n)]
