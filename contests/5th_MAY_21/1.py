size = len


def check(s):
    if len(set(list(s))) == len(s):
        return True
    else:
        ox = set()
        ox.add(s[0])
        dind = {s[0]: 0}
        for i in range(1, len(s)):
            if s[i] not in ox:
                ox.add(s[i])
                dind[s[i]] = i
            elif s[i] in ox and i == dind[s[i]] + 1:
                dind[s[i]] = i
            elif s[i] in ox and i != dind[s[i]] + 1:
                return False
        return True


tt = int(input())
for _ in range(tt):
    n = int(input())
    s = input()
    if len(s) > 1:
        if check(s):
            print("YES")
        else:
            print("NO")
    else:
        print("YES")
