# 2015-11-08  Runtime: 68 ms
class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        def dfs(L, k, oneAnswer):
            if k == 0:
                result.append(oneAnswer)
                return
            if len(L) < k:
                return
            for i in range(len(L)):
                dfs(L[i + 1:], k - 1, oneAnswer + [L[i]])

        result = []
        dfs(range(1, n + 1), k, [])
        return result