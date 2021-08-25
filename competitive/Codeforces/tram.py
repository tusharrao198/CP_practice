t = int(input())
lst = []
max_ = 0
exit_ = 0
enter_ = 0

for i in range(t):
    a, b = list(map(int, input().split()))
    lst.append(a)
    lst.append(b)
for i in range(2*t):
    if i == 0:
        exit_ = lst[i]
    if i == 1:
        enter_ = lst[i]
    if i%2 == 0 and i !=1 and i !=0:
        # exit_+=lst[i]
        enter_-= lst[i]
        continue
    if i % 2 != 0 and i != 1 and i != 0:
        enter_+=lst[i]
    if max_ < enter_:
        max_= enter_
print(max_)
        




