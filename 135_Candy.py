# 2015-02-09  Runtime: 129 ms

class Solution:
    # @param ratings, a list of integer
    # @return an integer
    def candy(self, ratings):
        length = len(ratings)
        res = [1 for i in xrange(length)]
        for i in xrange(length - 1):
            if ratings[i + 1] > ratings[i]:
                res[i + 1] = res[i] + 1
        for i in reversed(xrange(length - 1)):
            if ratings[i] > ratings[i + 1]:
                res[i] = max(res[i + 1] + 1, res[i])
        return sum(res)