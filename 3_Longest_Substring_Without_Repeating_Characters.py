# 2015-11-09  Runtime: 124 ms
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        lastAppear, L, maxLen = [-1] * 128, 0, 0
        for R in range(len(s)):
            # lastAppear[ord(s[R])] >= L is important bacause we only consider
            # letters inside the sliding window
            if lastAppear[ord(s[R])] != -1 and lastAppear[ord(s[R])] >= L:
                L = lastAppear[ord(s[R])] + 1
            lastAppear[ord(s[R])] = R
            maxLen = max(maxLen, R - L + 1)
        return maxLen