# 2014-12-24  Runtime: 320 ms

# Definition for a point
# class Point:
#     def __init__(self, a=0, b=0):
#         self.x = a
#         self.y = b

class Solution:
    # @param points, a list of Points
    # @return an integer
    def maxPoints(self, points):
        pointsNum = len(points)
        if pointsNum <= 2:
            return pointsNum
        # for each point, use dictionary slope to record point number of each slope
        # 对每个点，用字典slope记录每个斜率上点的个数
        res = -1
        for p1 in points:
            slope = {}
            samePointNum = 0
            for p2 in points:
                if p1 is not p2:
                    if p1.x == p2.x and p1.y == p2.y: # the same point
                        samePointNum += 1
                    elif p1.x != p2.x:
                        k = 1.0 * (p2.y - p1.y) / (p2.x - p1.x)
                        slope[k] = 2 if k not in slope else slope[k] + 1
                    else: # slope doesn't exist or is infinite, 斜率不存在的情况
                        slope['vertical'] = 2 if 'vertical' not in slope else slope['vertical'] + 1
            res = max(res, max(slope.values()) + samePointNum if slope else 1 + samePointNum)
        return res