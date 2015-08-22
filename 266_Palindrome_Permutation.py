# 2015-08-22  Runtime: 56 ms
class Solution(object):
    def canPermutePalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        count = {chr(i): 0 for i in xrange(128)}
        for ch in s:
            count[ch] += 1
        Sum = 0
        for ch in count:
            Sum += (count[ch] % 2)
        return Sum <= 1