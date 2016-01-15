# 2016-01-15,  61 tests, 268 ms
class Solution(object):
    def countRangeSum(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: int
        """
        n = len(nums)
        Sum, BITree = [0] * (n + 1), [0] * (n + 2)

        def count(x):
            s = 0
            while x:
                s += BITree[x]
                x -= (x & -x)
            return s

        def update(x):
            while x <= n + 1:
                BITree[x] += 1
                x += (x & -x)

        for i in range(n):
            Sum[i + 1] = Sum[i] + nums[i]
        sortSum, res = sorted(Sum), 0
        for sum_j in Sum:
            sum_i_count = count(bisect.bisect_right(sortSum, sum_j - lower)) - count(bisect.bisect_left(sortSum, sum_j - upper))
            res += sum_i_count
            update(bisect.bisect_left(sortSum, sum_j) + 1)
        return res
