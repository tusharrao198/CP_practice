def customerService (N, K, W, orders):
    # sort_me = sorted(orders, key=lambda x: x[0]) 
    
    # orders = [[3, 5], [4, 1], [4, 2], [10, 15], [15, 2]]
    orders = [[1,4], [2,2], [9,1]]
    time_=orders[0][0]+ orders[0][1]

    out_=[]
    for i in range(len(orders)):

        if i>0:
            if orders[i][0]>= (orders[i][1]+time_):
                out_.append((K*orders[i][1]) - (W*0))                    
                time_ = orders[i][1]
            else:
                out_.append((K*orders[i][1]) - (W*(time_-orders[i][0])))                    
                time_ += orders[i][1]
        if i==0:
            out_.append((K*orders[i][1]) - (W*0))
    return out_

# def sortme(orders):
#     lst = []
#     f = orders[0]
#     lst.append(f)
#     orders = orders[1:]
#     s = sorted(orders, key=lambda x: x[1]) 
#     lst.extend(s)
#     return lst


T = int(input())
for _ in range(T):
    N, K , W = list(map(int, input().split()))
    orders = []
    for i in range(N):
        orders.append(list(map(int, input().split())))    
    out_ = customerService(N, K, W, orders)
    print (' '.join(map(str, out_)))
    # print(sortme(orders))

# 1
# 5 10 1
# 3 5
# 4 2 
# 4 1
# 10 15 
# 15 2

# 1
# 3 5 1
# 1 4 
# 2 2
# 9 1
