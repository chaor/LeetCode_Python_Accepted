# 2015-06-03  Runtime: 144 ms
class Solution:
    # @param {integer[]} candidates
    # @param {integer} target
    # @return {integer[][]}
    def combinationSum(self, candidates, target):
        dp = [[] for i in xrange(target + 1)]
        dp[0].append([]) # dp[0] must have content, an empty list, i.e. dp[0] = [[]]
        for i in xrange(1, target + 1):
            for number in candidates:
                if i >= number:
                    for L in dp[i - number]:
                        tmp = sorted(L + [number])
                        if tmp not in dp[i]: dp[i].append(tmp)
        return dp[target]