# 2015-05-30 Runtime: 132 ms

# 首先转成求A和B数组中第k小的数的问题, 然后用k/2在A和B中分别找。比如k = 6, 分别看A和B中的第3个数, 
# 已知 A1 < A2 < A3 < A4 < A5... 和 B1 < B2 < B3 < B4 < B5..., 如果A3 <＝ B3, 
# 那么第6小的数肯定不会是A1, A2, A3, 因为最多有两个数小于A1, 三个数小于A2, 四个数小于A3。B3至少大于5个数, 
# 所以第6小的数有可能是B1 (A1 < A2 < A3 < A4 < A5 < B1), 有可能是B2 (A1 < A2 < A3 < B1 < A4 < B2), 
# 有可能是B3 (A1 < A2 < A3 < B1 < B2 < B3)。那就可以排除掉A1, A2, A3, 转成求A4, A5, ... B1, B2, B3, ...
# 这些数中第3小的数的问题, k就被减半了。每次都假设A的元素个数少, pa = min(k/2, lenA)的结果可能导致k == 1或A空, 
# 这两种情况都是终止条件。 
class Solution:
    # @param {integer[]} nums1
    # @param {integer[]} nums2
    # @return {float}
    def findMedianSortedArrays(self, nums1, nums2):
        mid = (len(nums1) + len(nums2)) / 2
        if (len(nums1) + len(nums2)) % 2:
            return self.findKthSmallest(nums1, nums2, mid + 1)
        else:
            return 0.5 * (self.findKthSmallest(nums1, nums2, mid) + self.findKthSmallest(nums1, nums2, mid + 1))
    
    # @param {integer} A, sorted list
    # @param {integer} B, sorted list
    # @param {integer} k
    # @return {double} the kth smallest number in A, B
    def findKthSmallest(self, A, B, k):
        # make sure len(A) < len(B)
        if len(A) > len(B): A, B = B, A
        if not A: return B[k-1]
        if not B: return A[k-1]
        if k == 1: return min(A[0], B[0])
        pa = min(len(A), k / 2)
        pb = k - pa
        return self.findKthSmallest(A[pa:], B, k - pa) if A[pa - 1] < B[pb - 1] else self.findKthSmallest(A, B[pb:], k - pb)


# 上面的解法每次需要创建新的列表，下面这种解法更省时， Runtime: 120 ms
class Solution:
    # @param {integer[]} nums1
    # @param {integer[]} nums2
    # @return {float}
    def findMedianSortedArrays(self, nums1, nums2):
        self.A, self.B, mid = nums1, nums2, (len(nums1) + len(nums2)) / 2
        if (len(nums1) + len(nums2)) % 2:
            return self.findKthSmallest(0, 0, mid + 1)
        else:
            return 0.5 * (self.findKthSmallest(0, 0, mid) + self.findKthSmallest(0, 0, mid + 1))
    
    # @param {integer} s1, start index of sorted list A
    # @param {integer} s2, start index of sorted list B
    # @param {integer} k
    # @return {double}, return kth smallest element in A, B
    def findKthSmallest(self, s1, s2, k):
        # make sure A is shorter
        if len(self.A) - s1 > len(self.B) - s2:
            self.A, self.B = self.B, self.A
            return self.findKthSmallest(s2, s1, k)
        if s1 >= len(self.A): return self.B[k-1]
        if s2 >= len(self.B): return self.A[k-1]
        if k == 1: return min(self.A[s1], self.B[s2])
        pa = min(len(self.A) - s1, k / 2)
        pb = k - pa
        return self.findKthSmallest(s1 + pa, s2, k - pa) if self.A[s1 + pa - 1] < self.B[s2 + pb - 1] \
            else self.findKthSmallest(s1, s2 + pb, k - pb)
