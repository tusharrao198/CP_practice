import sys
inp = sys.stdin.readline

n=int(inp())
a = ['I hate','I love']*50
print(*a[:n],sep=' that ',end=' it')