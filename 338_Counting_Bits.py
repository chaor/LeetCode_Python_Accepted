# 2016-03-17  16 tests, 771 ms
class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        result = [0]
        while len(result) < num + 1: result += [x + 1 for x in result]
        return result[:num + 1]

# 16 tests, 812 ms
class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        result = [0] * (num + 1)
        for i in xrange(1, num + 1): result[i] = result[i / 2] + i % 2
        return result
