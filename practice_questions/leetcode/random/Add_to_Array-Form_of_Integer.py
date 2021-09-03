class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        num = int("".join([str(_) for _ in num]))
        ans = num + k
        return [int(_) for _ in list(str(ans))]
