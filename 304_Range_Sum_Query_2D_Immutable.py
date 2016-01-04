# 2016-01-04  12 tests, 104 ms
# thanks to https://leetcode.com/discuss/69144/c-with-helper
class NumMatrix(object):
    def __init__(self, matrix):
        """
        initialize your data structure here.
        :type matrix: List[List[int]]
        """
        self.accu = [[0] * len(matrix[0]) for i in range(len(matrix))]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                self.accu[i][j] = matrix[i][j] + self.__a(i - 1, j) + self.__a(i, j - 1) - self.__a(i - 1, j - 1)

    def __a(self, i, j):
        ''' edge case '''
        return self.accu[i][j] if i >= 0 and j >= 0 else 0

    def sumRegion(self, row1, col1, row2, col2):
        """
        sum of elements matrix[(row1,col1)..(row2,col2)], inclusive.
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        return self.__a(row2, col2) - self.__a(row1 - 1, col2) - self.__a(row2, col1 - 1) + self.__a(row1 - 1, col1 - 1)

# Your NumMatrix object will be instantiated and called as such:
# numMatrix = NumMatrix(matrix)
# numMatrix.sumRegion(0, 1, 2, 3)
# numMatrix.sumRegion(1, 2, 3, 4)
