def compare_each(a, b): # comparing each list 
    c= 0
    for i in range(5):
        if a[i]<b[i]:
            c+=1
    return c>=3

def solve(dd, n):
    winner = 1
    for i in range(2, n+1):
        if compare_each(dd[i], dd[winner]):
            winner = i

    for i in range(1,n+1):
        if compare_each(dd[i], dd[winner]):
            winner = -1
            break
    print(winner)


tt = int(input())
for _ in range(tt):
    n = int(input())
    dd = {}
    for __ in range(1, n+1):
        dd[__] =  list(map(int, input().split()))
    solve(dd, n)
