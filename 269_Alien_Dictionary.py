# 2015-08-29  Runtime: 60 ms
# thanks to https://leetcode.com/discuss/54188/16-18-lines-python-29-lines-c
class Solution(object):
    def alienOrder(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        indegree, outdegree = collections.defaultdict(int), collections.defaultdict(set)
        for pair in [(words[i], words[i + 1]) for i in xrange(len(words) - 1)]:
            for a, b in zip(pair[0], pair[1]):
                if a != b:
                    outdegree[a].add(b)
                    indegree[b] += 1
                    break
        chars = set(''.join(words))
        free = chars - set(indegree)
        order = ''
        while free:
            a = free.pop()
            order += a
            for b in outdegree[a]:
                indegree[b] -= 1
                if indegree[b] == 0:
                    free.add(b)
        return order if set(order) == chars else ''