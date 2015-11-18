# 2015-11-17  Runtime: 84 ms
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        j, n = len(matrix[0]) - 1, len(matrix[0])
        for row in matrix:
            while j > 0 and row[j] > target: j -= 1
            if row[j] == target: return True
        return False