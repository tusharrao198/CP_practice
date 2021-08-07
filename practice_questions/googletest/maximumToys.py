# Ques 2. Maximum Toys

class Solution:
    def solution(self, arr, ans, cur, target, index, sum_):
        if sum_ == target:
            print(f"new pair = {cur[:]}")
            ans.append(len(cur[:]))

        elif sum_ < target:
            prev = -1
            for i in range(index, len(arr)):
                if prev != arr[i]:
                    cur.append(arr[i])
                    self.solution(
                        arr, ans, cur, target, i + 1, sum_ + arr[i]
                    )
                    # print("cur = ", cur)
                    x = cur.pop()
                    # print("pop = ", x)
                    prev = arr[i]
                    # print(f"prev= {prev}")
        return

    def maxToys(self, arr, broken, c):
        ans = []
        cur = []
        new = []
        for i in range(len(arr)):  # O(n)
            if arr[i] in broken:
                continue
            new.append(arr[i])
        # new.sort()  # O(nlogn)
        self.solution(new, ans, cur, c, index=0, sum_=0)
        return max(ans)  # O(n)


s = Solution()
c = 10
k = 2
broken = [2, 5]
arr = [3, 6, 2, 1, 4, 5]
ans = s.maxToys(arr, broken, c)
print(ans)
