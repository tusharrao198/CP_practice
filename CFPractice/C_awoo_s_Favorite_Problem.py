import sys
inp = sys.stdin.readline
for _ in range(int(inp())):
    n= int(inp())
    s1 = input()
    s2 = input()

    if s1.count('b') != s2.count('b'):
        print("NO")
        continue
    
    j=0
    for i in range(n):
        if s1[i]=="b":
            continue
        while j<len(s2) and s2[j]=="b":
            j+=1
        
        if (s1[i]!=s2[j] or (s1[i]=="a" and i>j) or (s1[i]=="c" and i<j)):
            print("NO")
            break
        j+=1
    else:
        print("YES")
