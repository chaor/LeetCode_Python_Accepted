# 2015-12-11  18 tests, 492 ms
class MedianFinder:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.largeHalf, self.smallHalf = [], []

    def addNum(self, num):
        """
        Adds a num into the data structure.
        :type num: int
        :rtype: void
        """
        heapq.heappush(self.smallHalf, -heapq.heappushpop(self.largeHalf, num))
        if len(self.smallHalf) > len(self.largeHalf):
            heapq.heappush(self.largeHalf, -heapq.heappop(self.smallHalf))

    def findMedian(self):
        """
        Returns the median of current data stream
        :rtype: float
        """
        if len(self.largeHalf) > len(self.smallHalf):
            return self.largeHalf[0]
        else:
            return (self.largeHalf[0] - self.smallHalf[0]) / 2.0

# Your MedianFinder object will be instantiated and called as such:
# mf = MedianFinder()
# mf.addNum(1)
# mf.findMedian()