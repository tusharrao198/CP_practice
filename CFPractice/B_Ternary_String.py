import sys
from math import inf

def createMap(t):
    track = {}
    for i in t:
        track[i] = track.get(i, 0) + 1
    return track


def minimumWindowSubstring(string, t):
    l, r = 0, 0
    min_size = float("inf")
    i = 0
    track = createMap(t)
    unique_values_count = len(track)

    while r < len(string):
        # print(r)
        if string[r] in track.keys():
            track[string[r]] -= 1
            if track[string[r]] == 0:
                unique_values_count -= 1

        while unique_values_count == 0:
            new_size = r - l + 1
            if new_size < min_size:
                min_size = new_size
                i = l
            if string[l] in track.keys():
                # print(string[l], l, r, track)
                track[string[l]] += 1
                if track[string[l]] == 1:
                    unique_values_count += 1
            l += 1
        r += 1

    if min_size != inf:
        # return string[i : min_size + i]
        return min_size
    return 0





inp = sys.stdin.readline
for _ in range(int(inp())):
    arr= inp()
    print(minimumWindowSubstring(arr, "123"))

