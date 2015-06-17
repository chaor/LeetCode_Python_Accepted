# 2015-06-16  Runtime: 120 ms
class Solution:
    # @param {string[]} strs
    # @return {string[]}
    def anagrams(self, strs):
        d = {}
        for s in strs:
            t = tuple(sorted(s))
            if t in d:
                d[t].append(s)
            else:
                d[t] = [s]
        result = []
        for group in d.values():
            if len(group) > 1: result += group
        return result