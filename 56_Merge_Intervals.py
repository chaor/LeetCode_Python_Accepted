# 2016-03-21   168 tests, 108 ms

# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        result, overlap, begin = [], 0, float('-inf')
        for x, y in sorted([(i.start, 1) for i in intervals] + [(i.end, -1) for i in intervals], key = lambda x:(x[0], -x[1])):
            if y == 1 and not overlap: begin = x
            if y == -1 and overlap == 1: result += Interval(begin, x),
            overlap += y
        return result
