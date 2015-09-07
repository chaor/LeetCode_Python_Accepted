# 2015-09-07  Runtime: 1712 ms

# The knows API is already defined for you.
# @param a, person a
# @param b, person b
# @return a boolean, whether a knows b
# def knows(a, b):

class Solution(object):
    def findCelebrity(self, n):
        """
        :type n: int
        :rtype: int
        """
        # thanks to https://leetcode.com/discuss/56350/straight-forward-c-solution-with-explaination
        # Use a two-pass scan, the first pass: find the candidate celebrity based on celebrity doesn't know any one
        candidate = 0
        for i in xrange(1, n):
            if not knows(i, candidate): candidate = i
        # second pass, verify this candidate, everyont should know him/her and he/she doesn't know any one
        for i in xrange(n):
            if i == candidate: continue
            if knows(candidate, i) or not knows(i, candidate): return -1
        return candidate