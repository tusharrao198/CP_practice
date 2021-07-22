n , m = list(map(int, input().split()))

lst = []
for kk in range(n):
    lst.append(list(input()))

marks = list(map(int, input().split()))

tot = []
for i in range(m):
    each_q = {"A": 0, "B": 0, "C": 0, "D": 0, "E": 0}
    for j in range(n):
        each_q[lst[j][i]] += 1
    c_max = max(list(each_q.values()))
    tot.append(marks[i]* c_max)
print(sum(tot))

    
