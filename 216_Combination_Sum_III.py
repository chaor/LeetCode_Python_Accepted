# 2015-11-09  Runtime: 44 ms
class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        def dfs(L, k, n, oneAnswer):
            if n < 0 or k < 0:
                return
            if not k and not n:
                result.append(oneAnswer)
                return
            for i in range(len(L)):
                dfs(L[i + 1:], k - 1, n - L[i], oneAnswer + [L[i]])
                    
        result = []
        dfs([1, 2, 3, 4, 5, 6, 7, 8, 9], k, n, [])
        return result