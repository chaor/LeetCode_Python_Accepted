# 2015-09-28  Runtime: 52 ms
class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        res = [10 ** 10] * len(triangle) # infinity
        res[0] = triangle[0][0]
        for i in xrange(1, len(triangle)):
            for j in xrange(i, 0, -1):
                res[j] = min(res[j], res[j - 1]) + triangle[i][j]
            res[0] += triangle[i][0]
        return min(res)