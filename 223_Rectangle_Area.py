# 2015-11-10  Runtime: 128 ms
class Solution(object):
    def computeArea(self, A, B, C, D, E, F, G, H):
        """
        :type A: int
        :type B: int
        :type C: int
        :type D: int
        :type E: int
        :type F: int
        :type G: int
        :type H: int
        :rtype: int
        """
        twoArea = (D - B) * (C - A) + (H - F) * (G - E)
        length, width = min(C, G) - max(A, E), min(D, H) - max(B, F)
        return twoArea - length * width if length > 0 and width > 0 else twoArea