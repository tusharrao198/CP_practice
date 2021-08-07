# Boolean Paranthesis memoization using map

global dp

dp = {}

def booleanParanthesis(arr, i, j, isTrue):
    if i > j: return True

    if  i==j:
        if isTrue: return arr[i] == "T"
        else: return arr[i] == "F"
        
    temp = [str(i), str(j), str(isTrue)]
    temp_key = "_".join(temp)

    if dp.get(temp_key) is not None:
        return dp[temp_key]

    _min = float("inf")

    ans = 0

    # initally i = 0 to j= len(arr) -1
    for k in range(i+1, j, 2):  # k from i+1 to <= j-1

        # temp answers
        lT = booleanParanthesis(arr,i, k-1, True)
        lF = booleanParanthesis(arr,i, k-1, False)    
        rT = booleanParanthesis(arr, k+1, j, True)
        rF = booleanParanthesis(arr, k+1, j, False)

        # AND
        if (arr[k] == "&"):
            if isTrue:
                ans += (lT * rT)
            else:
                ans+= (lF * rF ) + (lF*rT) + (lT*rF)

        # OR
        if (arr[k] == "|"):
            if isTrue:
                ans += (lT * rT ) + (lF*rT) + (lT*rF)
            else:
                ans+= (lF * rF )
        
        # XOR
        if (arr[k] == "^"):
            if isTrue:
                ans+= (lT*rF) + (lF*rT)
            else:
                ans+= (lF*rF) + (lT*rT)
    
    dp[temp_key] = ans
    return ans


# ----------------- main -----------------------------

_str = "T^F&T"
arr = list(_str)
i = 0
j = len(arr)-1
N = 1001  # arr.length given in constraints

isTrue = True # bcoz we finally want no. of ways for this expression to be True 

print(booleanParanthesis(arr, i, j, isTrue))
