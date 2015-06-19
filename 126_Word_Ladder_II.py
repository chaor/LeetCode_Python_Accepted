# 2015-06-18  Runtime: 712 ms

class Solution:
    # @param start, a string
    # @param end, a string
    # @param dict, a set of string
    # @return a list of lists of string
    def findLadders(self, start, end, dic):
        # thanks to https://leetcode.com/discuss/24191/defaultdict-for-traceback-and-easy-writing-lines-python-code
        dic.add(end)
        level = set([start])
        # key is word, value is parent word, e.g. {'hot': set(['hit']), 'cog': set(['log', 'dog'])}
        # In each level, defaultdict(set) can remove duplicates, first we need to get parent dictionary
        parents = collections.defaultdict(set)
        while level and end not in parents:
            next_level = collections.defaultdict(set)
            for word in level:
                for char in 'abcdefghijklmnopqrstuvwxyz':
                    for i in xrange(len(start)):
                        childWord = word[:i] + char + word[i+1:]
                        if childWord in dic and childWord not in parents: next_level[childWord].add(word)
            level = next_level
            parents.update(next_level)
            
        # then according parent dictionary, build result from end word to start word
        res = [[end]]
        while res and res[0][0] != start:
            res = [[p] + r for r in res for p in parents[r[0]]]
        return res