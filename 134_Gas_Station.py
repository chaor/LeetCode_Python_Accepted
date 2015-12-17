# 2015-10-01  Runtime: 40 ms
class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        if sum(gas) < sum(cost): return -1
        tank, index = 0, 0
        for i in xrange(len(gas)):
            tank += gas[i] - cost[i]
            if tank < 0:
                tank, index = 0, i + 1
        return index