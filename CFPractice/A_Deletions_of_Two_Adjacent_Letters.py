import sys
# from math import ceil, floor, gcd, sqrt, isqrt, pow, prod, log,
# from itertools import accumulate
def adjstr(st,s):
	for i in range(len(st)):
		if i%2==0 and st[i] == s:
			return True
	return False

inp = sys.stdin.readline
for _ in range(int(inp())):
    st= input()
    s = input()
    if adjstr(st,s) == True:
        print('YES')
    else:
        print("NO")

