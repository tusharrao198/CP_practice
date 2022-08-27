import heapq

arr = [2,3,45,6,8]
arr1 = [1, 34,5,26,7,78]
x = arr+arr1

heapq.heapify(x)
print(heapq.heappop(x))


