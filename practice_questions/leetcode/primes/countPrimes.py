class Solution:
    def countPrimes(self, n: int) -> int:
        if n<2: return 0
        arr = [True for _ in range(n)]
        arr[0] = arr[1] = False     
        for i in range(2, math.ceil(math.sqrt(n))):
            if arr[i]:  # True
                for j in range(i**2, n , i):  # multiples of i set to False
                    arr[j] = False
        return sum(arr)  # counts all True 
        
        