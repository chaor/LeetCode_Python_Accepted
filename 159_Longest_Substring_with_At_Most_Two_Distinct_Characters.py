# 2015-05-11  Runtime: 254 ms
class Solution:
    # @param {string} s
    # @return {integer}
    def lengthOfLongestSubstringTwoDistinct(self, s):
        count = {chr(i):0 for i in xrange(128)} # key is ASCII char 0 - 127, value is its count 
        startIndex, numDistinct, maxLen = 0, 0, 0
        for i in xrange(len(s)):
            if count[s[i]] == 0: numDistinct += 1
            count[s[i]] += 1
            while numDistinct > 2:
                count[s[startIndex]] -= 1
                if count[s[startIndex]] == 0: numDistinct -= 1
                startIndex += 1
            maxLen = max(i - startIndex + 1, maxLen)
        return maxLen