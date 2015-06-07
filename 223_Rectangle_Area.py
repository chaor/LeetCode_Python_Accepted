# 2015-06-07  Runtime: 57 ms
class Solution:
    # @param {integer} A
    # @param {integer} B
    # @param {integer} C
    # @param {integer} D
    # @param {integer} E
    # @param {integer} F
    # @param {integer} G
    # @param {integer} H
    # @return {integer}
    def computeArea(self, A, B, C, D, E, F, G, H):
        return (D - B) * (C - A) + (H - F) * (G - E) - (min(C, G) - max(A, E)) * (min(D, H) - max(B, F))