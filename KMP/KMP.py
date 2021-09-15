def computeLPSArray(pat, M, lps):
    len = 0  # length of the previous longest prefix suffix

    lps[0]  # lps[0] is always 0
    i = 1

    # the loop calculates lps[i] for i = 1 to M-1
    while i < M:
        if pat[i] == pat[len]:
            len += 1
            lps[i] = len
            i += 1
        else:
            # This is tricky. Consider the example.
            # AAACAAAA and i = 7. The idea is similar
            # to search step.
            if len != 0:
                len = lps[len-1]

                # Also, note that we do not increment i here
            else:
                lps[i] = 0
                i += 1


# txt = "ABABDABACDABABCABAB"
# pat = "ABABCABAB"

pat = "abede"
pat = pat[::-1] + "$" + pat
M = len(pat)
lps = [0]*M
print(computeLPSArray(pat, M , lps))
# KMPSearch(pat, txt)
print(lps)