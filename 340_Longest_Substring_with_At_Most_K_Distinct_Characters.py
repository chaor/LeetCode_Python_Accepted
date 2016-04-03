# 2016-04-02,  141 tests, 140 ms
class Solution(object):
    def lengthOfLongestSubstringKDistinct(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        charCount, left, distinct, result = [0] * 128, 0, 0, 0
        for right, ch in enumerate(s):
            ascii = ord(ch)
            if not charCount[ascii]: distinct += 1
            charCount[ascii] += 1
            while distinct > k:
                ascii = ord(s[left])
                if charCount[ascii] == 1: distinct -= 1
                charCount[ascii] -= 1
                left += 1
            result = max(result, right - left + 1)
        return result
