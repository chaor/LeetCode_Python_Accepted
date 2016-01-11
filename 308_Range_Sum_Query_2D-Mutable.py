# 2016-01-10  17 tests, 452 ms
class NumMatrix(object):
    def __init__(self, matrix):
        """
        initialize your data structure here.
        :type matrix: List[List[int]]
        """
        if not matrix or not matrix[0]: return
        self.m, self.n = len(matrix), len(matrix[0])
        self.tree = [[0] * (self.n + 1) for i in range(self.m + 1)]
        self.a = [[0] * self.n for i in range(self.m)]
        for i in range(self.m):
            for j in range(self.n):
                self.update(i, j, matrix[i][j])

    def update(self, row, col, val):
        """
        update the element at matrix[row,col] to val.
        :type row: int
        :type col: int
        :type val: int
        :rtype: void
        """
        diff, self.a[row][col], i = val - self.a[row][col], val, row + 1
        while i <= self.m:
            j = col + 1
            while j <= self.n:
                self.tree[i][j] += diff
                j += (j & -j)
            i += (i & -i)

    def __getSum(self, row, col):
        Sum = 0
        while row:
            j = col
            while j:
                Sum += self.tree[row][j]
                j -= (j & -j)
            row -= (row & -row)
        return Sum

    def sumRegion(self, row1, col1, row2, col2):
        """
        sum of elements matrix[(row1,col1)..(row2,col2)], inclusive.
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        return self.__getSum(row2 + 1, col2 + 1) - self.__getSum(row1, col2 + 1)\
                - self.__getSum(row2 + 1, col1) + self.__getSum(row1, col1)
