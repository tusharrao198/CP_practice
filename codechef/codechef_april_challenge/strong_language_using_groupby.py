from itertools import groupby
tc = int(input())
if tc in range(1, 11):
    for t in range(tc):
        n, k = list(map(int, input().split()))
        s = input()
        ch = [list(_)[0] for _, i in groupby(s) ]
        freq = [len(list(i)) for _, i in groupby(s) ]
        for j in range(len(ch)):
            if ch[j]=="*" and freq[j]>=k:
                print("YES")
                break
            elif (j == len(ch)-1):
                print("NO")
      

