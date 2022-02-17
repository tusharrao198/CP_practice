tt = int(input())
for _ in range(tt):
    n = int(input())
    arr=list(map(int, input().split()))
    arr.sort()
    bool_arr = arr
    # print(arr)
    ans = []
    for i in range(n//2):
        if bool_arr[i]!="T":
            ans.append(arr[i])
            bool_arr[i] = "T"

        if bool_arr[n-i-1]!="T":
            ans.append(arr[n-i-1])
            bool_arr[n-i-1] = "T"
        
        if bool_arr[i+1]!="T":
            ans.append(arr[i+1])
            bool_arr[i+1] = "T"

        if bool_arr[n-i-1]!="T":
            ans.append(arr[n-i-1])
            bool_arr[n-i-1] = "T"


    for i in ans[::-1]:
        print(i, end=" ")
    print()


#   0  1  2  3  4
# [-2, 4, 5, 5, 6]

# https://espresso.codeforces.com/789052e1f8c8408dbe8ed8a9a628b6d6aebb1b11.png

#  0   1  2  3  4  5
# [-2, 4, 5, 5, 6, 8]



# 1 2 5 5 5 5 
# 1 5 2 5 5 5