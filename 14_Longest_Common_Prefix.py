# 2015-06-02  Runtime: 68 ms
class Solution:
    # @param {string[]} strs
    # @return {string}
    def longestCommonPrefix(self, strs):
        if not strs: return ''
        k = 0
        while True:
            for str in strs:
                if not (k < len(str) and str[k] == strs[0][k]): return strs[0][:k]
            k += 1