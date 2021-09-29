# https://practice.geeksforgeeks.org/problems/consecutive-elements2306/1#submission


def removeConsecutiveCharacter(S):
    n = len(S)
    ans = ""
    for i in range(n - 1):
        if S[i] != S[i + 1]:
            ans += S[i]

    ans += S[n - 1]
    return ans
