# 2015-06-29   Runtime: 72 ms
class Solution:
    # @param {integer[]} nums
    # @return {integer[]}
    def majorityElement(self, nums):
        # thanks to https://leetcode.com/discuss/42806/boyer-moore-majority-vote-algorithm-generalization
        # there're at most 2 elements that appear more than ⌊ n/3 ⌋ times
        # m,n is the two most frequently appeared numbers
        m, n, mCount, nCount = 0, 1, 0, 0
        for i in nums:
            if i == m: mCount += 1
            elif i == n: nCount += 1
            elif mCount == 0: m, mCount = i, 1
            elif nCount == 0: n, nCount = i, 1
            else: mCount, nCount = mCount - 1, nCount - 1
            
        mCount, nCount = 0, 0
        for i in nums:
            if i == m: mCount += 1
            elif i == n: nCount += 1
        result = []
        if mCount > len(nums) / 3: result.append(m)
        if nCount > len(nums) / 3: result.append(n)
        return result