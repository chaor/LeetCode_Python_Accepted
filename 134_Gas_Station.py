# 2015-03-07 Runtime: 60 ms

class Solution:
    # @param gas, a list of integers
    # @param cost, a list of integers
    # @return an integer
    def canCompleteCircuit(self, gas, cost):
        # 如果sum(gas) < sum(cost)则无解, 否则必定有解。Sum < 0那一块不考虑, 因为total >= 0, 所以剩下那一块必定Sum >= 0。
        # if sum(gas) < sum(cost) then no answer, otherwise there will be a part whose Sum >= 0.
        ret, Sum, total = 0, 0, 0
        for i in xrange(len(gas)):
            Sum += gas[i] - cost[i]
            total += gas[i] - cost[i]
            if Sum < 0:
                ret = i + 1
                Sum = 0
        return ret if total >= 0 else -1