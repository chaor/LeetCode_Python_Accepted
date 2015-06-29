# 2015-06-28   Runtime: 101 ms
class Solution:
    # @param {string} s
    # @return {string}
    def shortestPalindrome(self, s):
        # thanks to https://leetcode.com/discuss/36987/python-solution-kmp
        # Actually we just need the last item of the KMP partial match table of s + '#' + s[::-1]
        # please see http://www.ruanyifeng.com/blog/2013/05/Knuth–Morris–Pratt_algorithm.html for KMP
        table, A = [0], s + '#' + s[::-1]
        for i in xrange(1, len(A)):
            maxMatchLen = table[i - 1]
            while maxMatchLen > 0 and A[maxMatchLen] != A[i]:
                maxMatchLen = table[maxMatchLen - 1]
            table.append(maxMatchLen + 1 if A[maxMatchLen] == A[i] else maxMatchLen)
        return s[table[-1]:][::-1] + s