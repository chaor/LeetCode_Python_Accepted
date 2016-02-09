# 2016-02-09 282 tests, 236 ms
# see https://leetcode.com/discuss/54724/python-140ms-beats-100%25-and-works-for-n-sum-n-2 for a faster solution


# from http://cs.stackexchange.com/questions/2973/generalised-3sum-k-sum-problem
#k-SUM can be solved more quickly as follows.

# For even k: Compute a sorted list S of all sums of k/2 input elements.
# Check whether S contains both some number x and its negation −x.
# The algorithm runs in O(n^(k/2)*logn) time.

# For odd k: Compute the sorted list S of all sums of (k−1)/2 input elements.
# For each input element a, check whether S contains both x and a−x, for some number x.
# (The second step is essentially the O(n2)-time algorithm for 3SUM.) The algorithm runs in O(n^(k+1)/2) time.

# Both algorithms are optimal (except possibly for the log factor when k is even and bigger than 2)
# for any constant k in a certain weak but natural restriction of the linear decision tree model of computation.
class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        d = collections.defaultdict(list)
        nums.sort()
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                d[nums[i] + nums[j]].append((i, j))
        result, j, k, keys = set(), 0, len(d) - 1, sorted(d)
        while j <= k:
            Sum = keys[j] + keys[k]
            if Sum == target:
                for i1, i2 in d[keys[j]]:
                    for i3, i4 in d[keys[k]]:
                        if i1 not in (i3, i4) and i2 not in (i3, i4):
                            result.add(tuple(sorted([nums[i1], nums[i2], nums[i3], nums[i4]])))
                while j < k and keys[j] == keys[j + 1]: j += 1
                while j < k and keys[k] == keys[k - 1]: k -= 1
                j, k = j + 1, k - 1
            elif Sum < target:
                while j < k and keys[j] == keys[j + 1]: j += 1
                j += 1
            else:
                while j < k and keys[k] == keys[k - 1]: k -= 1
                k -= 1
        return [list(t) for t in result]
