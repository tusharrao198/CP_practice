# # For inderstading logic
# # https://youtu.be/iwv1llyN6mo
#
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
    # print(track)

    while r < len(string):
        # print(r)
        if string[r] in track.keys():
            track[string[r]] -= 1
            if track[string[r]] == 0:
                unique_values_count -= 1
            # print(r, track, unique_values_count)

        while unique_values_count == 0:  # "TOTMTAPTAT"
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
        # print(min_size)
        return string[i: min_size + i]
    return ''


# s = "TOTMTAPTAT"
# t = "TTA"

# s = "ADOBECODEBANC"
# t = "ABC"

# s = "w"
# t = "o"

s = "xiEjBOGeHIMIlslpQIZ6jERaAVoHUc9Hrjlv7pQpUSY8oHqXoQYWWll8Pumov89wXDe0Qx6bEjsNJQAQ0A6K21Z0BrmM96FWEdRG69M9CYtdBOrDjzVGPf83UdP3kc4gK0uHVKcPN4HPdccm9Qd2VfmmOwYCYeva6BSG6NGqTt1aQw9BbkNsgAjvYzkVJPOYCnz7U4hBeGpcJkrnlTgNIGnluj6L6zPqKo5Ui75tC0jMojhEAlyFqDs7WMCG3dmSyVoan5tXI5uq1IxhAYZvRQVHtuHae0xxwCbRh6S7fCLKfXeSFITfKHnLdT65K36vGC7qOEyyT0Sm3Gwl2iXYSN2ELIoITfGW888GXaUNebAr3fnkuR6VwjcsPTldQSiohMkkps0MH1cBedtaKNoFm5HbH15kKok6aYEVsb6wOH2w096OwEyvtDBTQwoLN87JriLwgCBBavbOAiLwkGGySk8nO8dLHuUhk9q7f0rIjXCsQeAZ1dfFHvVLupPYekXzxtWHd84dARvv4Z5L1Z6j8ur2IXWWbum8lCi7aErEcq41WTo8dRlRykyLRSQxVH70rUTz81oJS3OuZwpI1ifBAmNXoTfznG2MXkLtFu4SMYC0bPHNctW7g5kZRwjSBKnGihTY6BQYItRwLUINApd1qZ8W4yVG9tnjx4WyKcDhK7Ieih7yNl68Qb4nXoQl079Vza3SZoKeWphKef1PedfQ6Hw2rv3DpfmtSkulxpSkd9ee8uTyTvyFlh9G1Xh8tNF8viKgsiuCZgLKva32fNfkvW7TJC654Wmz7tPMIske3RXgBdpPJd5BPpMpPGymdfIw53hnYBNg8NdWAImY3otYHjbl1rqiNQSHVPMbDDvDpwy01sKpEkcZ7R4SLCazPClvrx5oDyYolubdYKcvqtlcyks3UWm2z7kh4SHeiCPKerh83bX0m5xevbTqM2cXC9WxJLrS8q7XF1nh"
t = "dO4BRDaT1wd0YBhH88Afu7CI4fwAyXM8pGoGNsO1n8MFMRB7qugS9EPhCauVzj7h"

# print(s)
print(minimumWindowSubstring(s, t))
