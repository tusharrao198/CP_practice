import math
n, m, a, b = map(int, input().split())
if m*a<=b:
    print(n*a)
else:
    ans = (n//m)*b  + min((n%m)*a, b)
    print(ans)