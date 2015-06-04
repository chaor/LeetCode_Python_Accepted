# 2015-06-03  Runtime: 60 ms
# thanks to https://leetcode.com/discuss/17932/dp-solution-in-python
class Solution:
    # @param {integer} k
    # @param {integer} n
    # @return {integer[][]}
    def combinationSum3(self, k, n):
        # dp[x] is a set of tuples, e.g. when k=3, dp[7] = set([(1,2,4)])
        dp = [set() for i in xrange(n + 1)]
        for number in xrange(1, 10):
            if number > n: break
            for i in xrange(n - number, 0, -1):
                # set operation: s | t is equivalent to s.union(t)
                dp[number + i] |= {Tuple + (number,) for Tuple in dp[i] if len(Tuple) < k} 
            dp[number].add((number, ))
        return [list(Tuple) for Tuple in dp[n] if len(Tuple) == k]