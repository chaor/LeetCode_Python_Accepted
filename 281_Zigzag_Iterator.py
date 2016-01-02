# 2016-01-02  125 tests, 88 ms
class ZigzagIterator(object):

    def __init__(self, v1, v2):
        """
        Initialize your data structure here.
        :type v1: List[int]
        :type v2: List[int]
        """
        self.n = len(v1) + len(v2)
        self.gen = (v[i] for i in xrange(max(len(v1), len(v2))) for v in (v1, v2) if i < len(v))

    def next(self):
        """
        :rtype: int
        """
        self.n -= 1
        return next(self.gen)

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.n > 0

# Your ZigzagIterator object will be instantiated and called as such:
# i, v = ZigzagIterator(v1, v2), []
# while i.hasNext(): v.append(i.next())
