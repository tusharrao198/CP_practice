class Solution:
	# @param A : integer
	# @return a list of integers
	def sieve(self, A):
        arr = self.countPrimes(A)
        pos = []
        n = len(arr)
        for i in range(n):
            if arr[i]:
                pos.append(i)
        return pos

    def countPrimes(self, n):
        if n < 2:
            return [0]
        arr = [True for _ in range(n+1)]
        arr[0] = arr[1] = False
        for i in range(2, math.ceil(math.sqrt(n))+1):
            if arr[i]:  # True
                for j in range(i ** 2, n+1, i):  # multiples of i set to False
                    arr[j] = False
        return arr