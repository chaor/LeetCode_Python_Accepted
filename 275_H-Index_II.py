# 2015-09-05  Runtime: 52 ms
class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        N = len(citations) # note citations is in ascending order
        L, R = 0, N - 1
        while L <= R:
            M = (L + R) // 2
            if citations[M] >= N - M: # use [0, 1, 3, 5, 6] as an example
                R = M - 1
            else:
                L = M + 1
        return N - L # L is at the index which is just valid, R is just invalid