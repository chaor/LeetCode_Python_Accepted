# 2015-05-23  Runtime: 40 ms
class Solution:
    # @param {integer} m
    # @param {integer} n
    # @return {integer}
    def uniquePaths(self, m, n):
        # in total the robot will move m+n-2 steps, m-1 right, n-1 down
        # so the answer is C(m+n-2, m-1) = (m+n-2)! / ((m-1)!(n-1)!)
        return math.factorial(m + n - 2) / math.factorial(m - 1) / math.factorial(n - 1)