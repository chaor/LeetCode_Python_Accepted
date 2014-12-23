# 2014-12-23  Runtime: 112 ms
class Solution:
    # @param num, a list of integer
    # @return an integer
    def findMin(self, num):
        left, right = 0, len(num) - 1
        while True:
            if right - left <= 1:
                return min(num[left], num[right])
            mid = (left + right) / 2
            if num[right] < num[mid]: # pivot is in the right half, 转折点在右半部分
                left = mid
            else: # pivot is in the left half, 转正点在左半部分
                right = mid