import sys
from collections import deque

inp = sys.stdin.readline
for _ in range(int(inp())):
    n, q = map(int, inp().split())
    arr = list(map(int, inp().split()))
    queries = []
    max_round = -1
    for _ in range(q):
        j, k = map(int, inp().split())
        max_round = max(max_round, k)
        queries.append([j,k, _])
    # queries.sort(key=lambda x:x[1])

    # sorted_queries = sorted(queries, key=lambda x:-x[1])
    # max_round = sorted_queries[0][1]

    qu = deque(arr)
    mx = max(arr)
    wins = {kk:0 for kk in range(1, n+1)}
    ans = dict() # storing queries answer of each round
    rounds = 0

    while qu[0]!=mx:
        if qu[0]>qu[1]:
            qu[0], qu[1] = qu[1], qu[0]
            x = qu.popleft()
        else:
            x = qu.popleft()
        qu.append(x)
        rounds+=1
        wins[qu[0]] = wins.get(qu[0], 0) + 1
        ans[rounds] = wins
        # print("qu = ", qu, ans)

    # print(f"max_round = {max_round}, rounds = {rounds}")

    # print(ans,' --- ' ,wins)
    # if rounds == 0 then ans array is empty
    for i  in range(q):
        # print("query = ", queries[i])
        idx = queries[i][0] - 1
        val = arr[idx]
        # print(idx, val)
        rnd = queries[i][1]
        
        left_round = rnd - rounds
        if rounds==0:
            res = wins[val] + left_round
        else:
            if rnd>rounds:
                if val==mx:
                    res = ans[rounds][val] + left_round
                else:
                    res = ans[rounds][val]
            else:
                res = ans[rnd][val]
        print(res)