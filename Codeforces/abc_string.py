t = int(input())

def check_bool(x, zeros, val):
    for j in zeros:
        x[j] = val
    count =0
    for kk in range(len(x)):
        count+= x[kk]
        if count< 0:
            return False
    if count==0:
        return True
    else:
        return False
        
def check(s):
    ddd = {"A":0, "B":0, "C":0}
    nn = []
    if s[0]==s[-1]:
        return "NO"
    if s[0]=="A":
        ddd["A"] = 1
    elif s[-1] == "A":
        ddd["A"] = -1
    if s[0] == "B":
        ddd["B"] = 1
    elif s[-1] == "B":
        ddd["B"] = -1
    if s[0] == "C":
        ddd["C"] = 1
    elif s[-1] == "C":
        ddd["C"] = -1

    for i in range(len(s)):
        nn.append(ddd[s[i]])

    lst_plus = nn
    lst_sub = nn

    index_zero = []
    for i in range(len(nn)):
        if nn[i]==0:
            index_zero.append(i)
    if check_bool(lst_plus, index_zero, 1) or check_bool(lst_sub, index_zero, -1):
        return "YES"
    else:
        return "NO"

for i in range(t):
    s = input()
    print(check(s))