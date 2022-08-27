import sys
inp = sys.stdin.readline
for _ in range(int(inp())):
    n= int(inp())
    s=input()
    arr = [int(_) for _ in s]
    if arr==sorted(arr):
        print(s)
    else:
        pack = [[arr[0]]]
        x = 0
        for i in range(1, n):
            if arr[i]==arr[i-1]:
                pack[x].append(arr[i])
            else:
                x = x+1
                pack.append([arr[i]])

        packlen = len(pack)
        # print(pack)
        c = ""
        if pack[0][0]==0:            
            c += "0"*(len(pack[0])+1)
        elif pack[0][0]!=0:            
            c += "0"
        if pack[-1][0]==1:
            c += "1"*len(pack[-1])
        
        print(c)
        
