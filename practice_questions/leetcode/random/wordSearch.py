from typing import List

# https://leetcode.com/problems/word-search/submissions/
class Solution:
    dir_x = [0, 0, 1, -1]
    dir_y = [1, -1, 0, 0]

    def solution(self, board, word, x, y, cur):
        if (
            x not in range(0, len(board))
            or y not in range(0, len(board[x]))
            or board[x][y] == " "
        ):
            # print("range error")
            return False

        temp = board[x][y]
        cur += temp
        cur_len = len(cur)
        if cur_len > len(word):
            return False

        if word[cur_len - 1] != cur[cur_len - 1]:
            return False

        if cur == word:
            return True

        board[x][y] = " "
        for i in range(4):
            if self.solution(board, word, x + self.dir_x[i], y + self.dir_y[i], cur):
                return True

        board[x][y] = temp
        return False

    def exist(self, board: List[List[str]], word: str) -> bool:
        if len(word) == 0:
            return True
        for row in range(len(board)):
            for col in range(len(board[row])):
                if word[0] == board[row][col] and self.solution(
                    board, word, row, col, ""
                ):
                    return True
        return False


s = Solution()
arr = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
w = "SEE"
ans = s.exist(arr, w)
print(ans)
