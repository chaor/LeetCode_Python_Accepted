# 2015-09-17  Runtime: 84 ms
# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def canAttendMeetings(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: bool
        """
        intervals.sort(key = lambda x: x.start)
        return all(intervals[i - 1].end <= intervals[i].start for i in xrange(1, len(intervals)))