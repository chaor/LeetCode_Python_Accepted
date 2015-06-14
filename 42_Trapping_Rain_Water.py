# 2015-06-14  Runtime: 76 ms
class Solution:
    # @param {integer[]} height
    # @return {integer}
    def trap(self, height):
        # thanks to https://leetcode.com/discuss/16171/sharing-my-simple-c-code-o-n-time-o-1-space
        L, R, maxL, maxR, A, res = 0, len(height) - 1, 0, 0, height, 0
        while L <= R:
            if A[L] <= A[R]:
                if A[L] >= maxL: maxL = A[L]
                else: res += maxL - A[L]
                L += 1
            else:
                if A[R] >= maxR: maxR = A[R]
                else: res += maxR - A[R]
                R -= 1
        return res