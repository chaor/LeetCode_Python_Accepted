# 2015-07-31  Runtime: 76 ms
class Solution:
    # @param {string} s
    # @param {string} t
    # @return {boolean}
    def isAnagram(self, s, t):
        count = [0 for i in xrange(26)]
        for c in s:
            count[ord(c) - ord('a')] += 1
        for c in t:
            count[ord(c) - ord('a')] -= 1
        for num in count:
            if num: return False
        return True