
l=int(input())
lst = list(map(int, input().split()))
ans=(l * (l + 1) // 2) - sum(lst)
print(ans)