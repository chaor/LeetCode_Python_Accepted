# 2015-05-10  Runtime: 154 ms
class Solution:
    # @param {string} s
    # @return {integer}
    def lengthOfLongestSubstring(self, s):
        # key: ASCII 0 - 128, value:  last time appearance index of this char
        lastTimeIndex = {chr(i):-1 for i in xrange(128)}
        noRepeatingSinceThis, substringMaxLen = 0, 0
        for i in xrange(len(s)):
            if lastTimeIndex[s[i]] >= noRepeatingSinceThis:
                noRepeatingSinceThis = lastTimeIndex[s[i]] + 1
            lastTimeIndex[s[i]] = i
            substringMaxLen = max(i - noRepeatingSinceThis + 1, substringMaxLen)
        return substringMaxLen