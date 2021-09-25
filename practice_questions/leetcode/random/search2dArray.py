from typing import List

# https://leetcode.com/problems/search-a-2d-matrix/submissions/


# O(n) approach
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])
        if rows == 0:
            return False

        smallest = matrix[0][0]
        largest = matrix[rows - 1][cols - 1]

        if (target < smallest) or (target > largest):
            return False

        i, j = 0, cols - 1
        while i < rows and j >= 0:
            if matrix[i][j] == target:
                return True
            if matrix[i][j] > target:
                j -= 1
            else:
                i += 1
        return False


s = Solution()
matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
target = 16
print(s.searchMatrix(matrix, target))
