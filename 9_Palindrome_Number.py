# 2015-05-11  Runtime: 265 ms
class Solution:
    # @param {integer} x
    # @return {boolean}
    def isPalindrome(self, x):
        if x < 0: return False
        div = 1
        while x / div >= 10: div *= 10
        while x:
            if x / div != x % 10: return False
            x = (x % div) / 10
            div /= 100
        return True