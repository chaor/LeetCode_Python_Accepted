# 2015-06-13  Runtime: 52 ms
class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer[]}
    def searchRange(self, nums, target):
        self.nums, self.target = nums, target
        return self.search(0, len(self.nums) - 1)
        
    def search(self, L, R):
        if L == R:
            return [L, L] if self.nums[L] == self.target else [-1, -1]
        while L <= R:
            M = (L + R) / 2
            if self.target > self.nums[M]:
                L = M + 1
            elif self.target < self.nums[M]:
                R = M - 1
            else: # self.target == self.nums[M]
                left, right = self.search(L, M - 1), self.search(M + 1, R)
                return [M if left[0] == -1 else left[0], M if right[1] == -1 else right[1]]
        return [-1, -1]