# 2015-06-03  Runtime: 68 ms
class Solution:
    # @param {integer[]} candidates
    # @param {integer} target
    # @return {integer[][]}
    def combinationSum2(self, candidates, target):
        # dp[x] is a set of tuples, e.g. dp[8] = set([(1,7), (1,2,5), (2,6), (1,1,6)])
        dp = [set() for i in xrange(target + 1)]
        candidates.sort()
        for number in candidates:
            if number > target: break
            for i in xrange(target - number, 0, -1):
                # set operation: s | t is equivalent to s.union(t)
                dp[number + i] |= {Tuple + (number,) for Tuple in dp[i]} 
            dp[number].add((number, ))
        return [list(Tuple) for Tuple in dp[target]]