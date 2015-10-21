# 2015-10-20  Runtime: 104 ms
# Definition for a point.
# class Point(object):
#     def __init__(self, a=0, b=0):
#         self.x = a
#         self.y = b

class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[Point]
        :rtype: int
        """
        if len(points) <= 2: return len(points)
        result = 0
        for p1 in points:
            d, d_max, vertical, same = {}, 0, 0, 0
            for p2 in points:
                if p2.x == p1.x:
                    if p2.y == p1.y:
                        same += 1
                    else:
                        vertical += 1
                else:
                    k = (p2.y - p1.y) * 1.0 / (p2.x - p1.x)
                    d[k] = d[k] + 1 if k in d else 1
                    d_max = max(d_max, d[k])
            result = max(result, d_max + same, vertical + same)
        return result