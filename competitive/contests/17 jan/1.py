t = int(input())
def fun(t):
    lst = list(input())
    if len(lst)%2!=0:
        return "NO"
    else:
        if lst[0]==")":
            return "NO"
        if lst.count("?")==0:
            if lst.count(")")==lst.count("("):
                return "YES" 
            else:
                return "NO"
        if lst.count("?")>0:
            for j in range(len(lst)):
                if lst[j]=="?" and lst[j+1]=="?":
                    lst[j]="("
                    lst[j+1]=")"

        else:
            return "NO"
for i in range(t):
    print(fun(t))

