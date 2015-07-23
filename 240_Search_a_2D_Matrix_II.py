# 2015-07-22  Runtime: 104 ms
class Solution:
    # @param {integer[][]} matrix
    # @param {integer} target
    # @return {boolean}
    def searchMatrix(self, matrix, target):
        # thanks to https://leetcode.com/discuss/47571/4-lines-c-6-lines-ruby-7-lines-python-1-liners
        # 右上角开始向左向下扫，O(m + n)
        j = -1
        for row in matrix:
            while j + len(row) > 0 and row[j] > target:
                j -= 1
            if row[j] == target:
                return True
        return False