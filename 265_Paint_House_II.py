# 2015-12-26  105 tests, 52 ms
class Solution(object):
    def minCostII(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        if not costs or not costs[0]:
            return 0
        n, k = len(costs), len(costs[0])
        # min1 is the minimal cost of current round, min2 is the secone minimal
        min1, min2, idx1 = 0, 0, -1
        for i in range(n):
            next1, next2, nidx1 = sys.maxint, sys.maxint, -1
            for j in range(k):
                # make sure no same color with previous house
                x = costs[i][j] + (min2 if j == idx1 else min1)
                if x < next1:
                    next1, next2, nidx1 = x, next1, j
                elif x < next2:
                    next2 = x
            min1, min2, idx1 = next1, next2, nidx1
        return min1
