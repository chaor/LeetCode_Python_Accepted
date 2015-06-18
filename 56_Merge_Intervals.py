# 2015-06-17  Runtime: 102 ms

# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    # @param {Interval[]} intervals
    # @return {Interval[]}
    def merge(self, intervals):
        if len(intervals) == 0: return []
        intervals.sort(key = lambda x: x.start)
        result = [intervals[0]]
        for i in intervals:
            if i.start > result[-1].end:
                result.append(i)
            else:
                result[-1].end = max(result[-1].end, i.end)
        return result