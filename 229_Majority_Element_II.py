# 2015-11-10   Runtime: 52 ms
# Boyer-Moore Majority Vote algorithm, http://www.cs.utexas.edu/~moore/best-ideas/mjrty/
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        countA, countB, A, B = 0, 0, 5, 15 # initialize A, B to random values
        for x in nums:
            if x == A:
                countA += 1
            elif x == B:
                countB += 1
            elif countA == 0:
                A, countA = x, 1
            elif countB == 0:
                B, countB = x, 1
            else:
                countA, countB = countA - 1, countB - 1
        res = []
        if nums.count(A) > len(nums) // 3:
            res.append(A)
        if nums.count(B) > len(nums) // 3:
            res.append(B)
        return res