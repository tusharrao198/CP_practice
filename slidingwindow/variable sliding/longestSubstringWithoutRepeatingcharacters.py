
def longestSubstringWithoutRepeatingChar(arr, n ):
    i = j = 0
    mp = {}
    maxlength = float("-inf")

    while j<n:

        mp[arr[j]] = mp.get(arr[j], 0)+1
        
        if len(mp)==j-i+1:
            maxlength = max(maxlength, j-i+1)
            j+=1
    
        elif len(mp) < j-i+1:

            while len(mp) <j-i+1:
                mp[arr[i]]-=1
                if mp[arr[i]]==0:
                    mp.pop(arr[i])
                i+=1
            j+=1
        # print(mp, i, j)
    print(ss[i:j])
    return maxlength


ss = "pwwkew"
n = len(ss)
print(longestSubstringWithoutRepeatingChar(ss, n))
        