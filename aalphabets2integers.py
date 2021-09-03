
import string
lower = {v : k+1 for k, v in enumerate(string.ascii_lowercase)}

upper = {v: k+1 for k, v in enumerate(string.ascii_uppercase)}
print(upper)

def alph2int(s):
    ans = ""
    for i in s:
        ans = ans + str(upper[i])
    return ans


s = "GOVERNMENT"
print(alph2int(s))
