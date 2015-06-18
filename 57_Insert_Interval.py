# 2015-06-17  Runtime: 84 ms

# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    # @param {Interval[]} intervals
    # @param {Interval} newInterval
    # @return {Interval[]}
    def insert(self, intervals, newInterval):
        result, i = [], 0
        # add all intervals ending before newInterval starts
        while i < len(intervals) and intervals[i].end < newInterval.start:
            result.append(intervals[i])
            i += 1
        # merge all overlapping intervals to one considering newInterval
        while i < len(intervals) and intervals[i].start <= newInterval.end:
            newInterval.start, newInterval.end = min(newInterval.start, intervals[i].start), max(newInterval.end, intervals[i].end)
            i += 1
        result.append(newInterval) # add the union of intervals we got
        # add all the rest
        while i < len(intervals): 
            result.append(intervals[i])
            i += 1
        return result