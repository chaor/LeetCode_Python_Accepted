# 2015-11-28   20 tests, 40 ms
class Solution(object):
    def getFactors(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        self.result = []
        self.solve(n, 2, [])
        return self.result
        
    def solve(self, n, x, oneAnswer):
        while x * x <= n:
            if n % x == 0 and n / x >= x:
                self.result.append(oneAnswer + [x, n / x])
                self.solve(n / x, x, oneAnswer + [x])
            x += 1