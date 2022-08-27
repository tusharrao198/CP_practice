def climbingLeaderboard(ranked, player):
    # Write your code here
    r,p=len(ranked), len(player)
    ranked= list(set(ranked))
    ans=[]
    for j in range(p):
        ranked.append(player[j])
        ranked = list(set(ranked))
        ranked.sort(reverse=True)
        ans.append(ranked.index(player[j])+1)
    return ans

player=[70,80,105]
ranked=[100,90,90,80]

x=climbingLeaderboard(ranked, player)
print(x)