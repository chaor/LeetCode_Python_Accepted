# 2014-12-20  Runtime: 160 ms
class Solution:
    # @param num, a list of integer
    # @return an integer
    def findPeakElement(self, num):
        left, right = 0, len(num) - 1
        while left < right:
            if right - left == 1:
                return left if num[left] > num[right] else right
            mid = (left + right) / 2
            if num[mid] > num[mid + 1]:
                right = mid
            else:
                left = mid
        return left