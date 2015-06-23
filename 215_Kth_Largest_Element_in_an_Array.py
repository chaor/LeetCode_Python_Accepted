# 2015-06-22  Runtime: 48 ms
# thanks to https://leetcode.com/discuss/38336/solution-using-quicksort-solution-using-heapsort-both-space
class Solution:
    # @param {integer[]} nums
    # @param {integer} k
    # @return {integer}
    def findKthLargest(self, nums, k):
        L, R = 0, len(nums) - 1
        while L <= R:
            pos = self.partition(L, R, nums)
            if pos == k - 1: return nums[pos]
            if pos > k - 1:
                R = pos - 1
            else:
                L = pos + 1
        
    # @param {integer} left
    # @param {integer} right
    # @return {integer}
    def partition(self, L, R, A):
        M = (L + R) / 2
        pivot = A[L] + A[R] + A[M] - max(A[L], A[R], A[M]) - min(A[L], A[R], A[M])
        pivotIndex = L if pivot == A[L] else R if pivot == A[R] else M
        A[pivotIndex], A[L] = A[L], A[pivotIndex]
        left, right = L + 1, R
        while left <= right:
            if A[left] < pivot and A[right] > pivot:
                A[left], A[right] = A[right], A[left]
                left += 1
                right -= 1
            if A[left] >= pivot: left += 1
            if A[right] <= pivot: right -= 1
        A[right], A[L] = A[L], A[right]
        return right