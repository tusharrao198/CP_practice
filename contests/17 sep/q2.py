test = int(input())


def ans2(test):
    for i in range(test):
        n = int(input())
        s = input()
        lst = list(s)
        a = lst.index("2")
        b = lst[a + 1 :].index("2")
        if lst.count("2") >= 2 and lst.count("0") >= 2:
            for l in range(len(lst) - 1):
                if lst[l] == "2" and lst[l + 1] == "2":
                    return "NO"
                if lst[l] == "0" and lst[l + 1] == "0":
                    return "NO"

            if lst[a + 1 : b].count("0") == 1 and lst[b + 1 :].count("0") == 1:
                return "YES"
            elif s == "2020":
                return "YES"
        else:
            return "NO"


print(ans2(test))