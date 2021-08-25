n = list(map(int, input().split()))
count_ = {}
for i in range(3):
    count_[n[i]] = count_.get(n[i], 0) +1
cc = list(count_.values())
for i in range(len(cc)):
    if cc[i]>=2:
        print("YES")
        break
    elif i==(len(cc)-1):
        print("NO")
        