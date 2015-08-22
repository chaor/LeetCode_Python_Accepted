# 2015-08-22  Runtime: 96 ms
class Vector2D(object):
    
    # thanks to https://leetcode.com/discuss/50292/7-9-lines-added-java-and-c-o-1-space
    def __init__(self, vec2d):
        """
        Initialize your data structure here.
        :type vec2d: List[List[int]]
        """
        self.i, self.j = iter(vec2d), None

    def next(self):
        """
        :rtype: int
        """
        return self.j.next()

    def hasNext(self):
        """
        :rtype: bool
        """
        while (not self.j or self.j.__length_hint__() == 0) and self.i.__length_hint__() > 0:
            self.j = iter(self.i.next())
        return self.j and self.j.__length_hint__() > 0

# Your Vector2D object will be instantiated and called as such:
# i, v = Vector2D(vec2d), []
# while i.hasNext(): v.append(i.next())