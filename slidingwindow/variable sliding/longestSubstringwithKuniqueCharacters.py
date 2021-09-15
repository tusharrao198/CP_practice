
# variable sliding technique 
# elements can be repeating
def longestSubstringwithKUniqueChar(arr, n , k):
    i = j = 0
    maxlength = float("-inf")
    mp = {} # map
    while j<n:
        mp[arr[j]] = mp.get(arr[j], 0) + 1

        if len(mp)<k:
            j+=1
        
        elif len(mp)==k:
            maxlength = max(maxlength, j-i+1)
            j+=1
        
        elif len(mp)>k:

            while len(mp)>k:
                mp[arr[i]]-=1
                if mp[arr[i]]==0:
                    mp.pop(arr[i])
                i+=1
            j+=1
    
    return maxlength


ss = "aabacebebebe"
ss = "ababacdefffg"
n = len(ss)
k =3
print(longestSubstringwithKUniqueChar(ss, n , k))