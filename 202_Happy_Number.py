# 2015-04-21  Runtime: 63 ms

class Solution:
    # @param {integer} n
    # @return {boolean}
    def isHappy(self, n):
        visited = set()
        while True:
            sum = 0
            while n:
                sum += (n % 10) ** 2
                n /= 10
            if sum == 1: return True
            if sum in visited: return False
            visited.add(sum)
            n = sum