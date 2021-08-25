tz, h, x = list(map(int, input().split()))
tz_s = list(map(int, input().split()))

if tz in range(1, 101) and x < h:
    for i in range(len(tz_s)):
        if tz_s[i] in range(1, 101):
            if tz_s[i] + x >= h:
                print("YES")
                break
            if i + 1 == len(tz_s) and tz_s[i] + x < h:
                print("NO")
                break
