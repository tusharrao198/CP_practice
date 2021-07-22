t = int(input())
a = 2050
for test in range(t):
    n = int(input())
    if n % a:
        print(-1)
    else:
        m = str(int(n / a))
        sum_ = 0
        for i in m:
            sum_ += int(i)
        print(sum_)
