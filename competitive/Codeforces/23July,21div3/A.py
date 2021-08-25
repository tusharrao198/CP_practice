tt = int(input())
for _ in range(tt):
    num = int(input())
    x = num//3
    twos = x
    ones = num - (2*twos)
    aa = abs(ones-twos)
    if aa==0 or aa==1:
        print(ones, twos)
    elif aa==2:
        while True:
            if aa ==1:
                print(ones, twos)
                break
            if ones > twos and aa==2:
                twos+=1
                ones-=2
                aa = abs(twos-ones)
            else:
                break
    else:
        print(ones,twos)





