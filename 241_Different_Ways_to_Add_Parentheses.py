# 2015-07-27  Runtime: 80 ms
class Solution:
    # @param {string} input
    # @return {integer[]}
    def diffWaysToCompute(self, input):
        # thanks to https://leetcode.com/discuss/48468/1-11-lines-python
        return [a + b if c == '+' else a - b if c == '-' else a * b
            for i, c in enumerate(input) if c in '+-*'
            for a in self.diffWaysToCompute(input[:i])
            for b in self.diffWaysToCompute(input[i + 1:])] or [int(input)]