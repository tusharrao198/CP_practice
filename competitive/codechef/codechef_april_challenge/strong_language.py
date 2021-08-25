    tc = int(input())
    if tc in range(1, 11):
        for t in range(tc):
            n, k = list(map(int, input().split()))
            s = input()
            count =0
            for i in range(len(s)):
                if s[i] == "*":
                    count+=1
                else:
                    count= 0# cook your dish here
                if count>=k:
                    print("YES")
                    break
                if i==(len(s)-1):
                    print("NO")