# 2015-09-18  Runtime: 80 ms
# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        # thanks to https://leetcode.com/discuss/50948/c-o-n-log-n-584-ms-3-solutions
        roomRequire = []
        for i in intervals:
            roomRequire += [(i.start, 1), (i.end, -1)]
        roomRequire.sort()
        res, roomNum = 0, 0
        for i in roomRequire:
            roomNum += i[1]
            if roomNum > res: res = roomNum
        return res