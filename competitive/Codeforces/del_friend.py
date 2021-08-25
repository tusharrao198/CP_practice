t = int(input())
for i in range(t):
    count = 0
    n, k = list(map(int, input().split()))
    lst = list(map(int, input().split()))
    removed = 0 
    # print("LS",lst)
    # while (k!=0 and k>0):
    #     print("ASDF", count, "len", len(lst)-1)
    #     if (count<(len(lst)-1)):
    #         print("SS",count)
    #         if lst[count]< lst[count+1]:
    #             lst.remove(lst[count])
    #             count=0
    #             print("hello1")
    #         else:
    #             print("ASDGGHH")
    #             count+=1
    #     else:
    #         break

    while (count < (len(lst)-1)):
        if removed == k:
            break
        if lst[count] < lst[count+1]:
            lst.remove(lst[count])
            if count != 0:
                count -= 1
            count -= 1
            removed += 1
        count += 1

    while removed < k :
        lst.remove(lst[-1])
        removed += 1

    print(lst)

 
