def jumpingOnClouds(c):
    # Write your code here
    count = 0
    i = 0
    while i < len(c) - 2:
        if c[i] == 0 and c[i + 1] == 0 and c[i + 2] == 0:
            count += 1
            i += 2
        elif c[i] == 0 and c[i + 1] != 0 and c[i + 2] == 0:
            count += 1
            i += 2
        else:
            i += 1
            count += 1
    if i<len(c)-1:
        count+=1
        
    return count


# c = [0, 0, 0, 0, 1, 0]
# c = [0, 0, 1, 0, 0, 1, 0]
c = [0, 0, 0, 1, 0, 0]
result = jumpingOnClouds(c)
print(result)

#    x,y = 0,0
#     while x<len(c)-2:
#         x = x+1 if c[x+2] else x+2
#         y+=1
#     if x<len(c)-1:
#         y+=1
#     return y
