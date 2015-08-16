# 2015-08-15  Runtime: 232 ms
class Solution:
    # @param {string[]} strs
    # @return {string[][]}
    def groupAnagrams(self, strs):
        d = {}
        for word in strs:
            t = tuple(sorted(word))
            if t in d:
                d[t].append(word)
            else:
                d[t] = [word]
        for key in d: d[key].sort()
        return d.values()