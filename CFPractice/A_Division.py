import sys
inp = sys.stdin.readline
for _ in range(int(inp())):
    n= int(inp())
    if n<=1399:
        print("Division 4")
    elif 1400<=n<=1599:
        print("Division 3")        
    elif 1600<=n<=1899:
        print("Division 2")
    elif n>=1900:
        print("Division 1")
        
    