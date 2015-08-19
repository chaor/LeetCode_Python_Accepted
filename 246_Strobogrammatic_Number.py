# 2015-08-18  Runtime: 44 ms

class Solution:
    # @param {string} num
    # @return {boolean}
    def isStrobogrammatic(self, num):
        L, R = 0, len(num) - 1
        while L < R:
            if (num[L], num[R]) not in (('0', '0'), ('1', '1'), ('8', '8'), ('6', '9'), ('9', '6')): return False
            L, R = L + 1, R - 1
        if L == R: return num[L] in '018'
        return True