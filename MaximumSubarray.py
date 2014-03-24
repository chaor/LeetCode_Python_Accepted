# Accepted on 03/24/2014, runtime: 244 ms
class Solution:
    # @param A, a list of integers
    # @return an integer
    def maxSubArray(self, A):
        lenA = len(A)
        s = [0 for i in xrange(lenA)] # s[i] is maximum subarray ends in A[i]
        s[0] = A[0]
        for i in xrange(1, lenA):
            s[i] = s[i-1] + A[i] if s[i-1] > 0 else A[i]
        return max(s)
