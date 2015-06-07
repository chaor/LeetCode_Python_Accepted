# 2015-06-06  Runtime: 228 ms
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
class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer[][]}
    def fourSum(self, nums, target):
        if len(nums) < 4: return []
        s = {} # key is sum, value is tuple(index1, index2)
        for i in xrange(len(nums)):
            for j in xrange(i + 1, len(nums)):
                Sum = nums[i] + nums[j]
                if Sum in s:
                    s[Sum].append((i, j))
                else:
                    s[Sum] = [(i, j)]
        sortedKeys = sorted(s.keys())
        L, R, result = 0, len(sortedKeys) - 1, set([])
        while L <= R:
            if sortedKeys[L] + sortedKeys[R] > target: R -= 1
            elif sortedKeys[L] + sortedKeys[R] < target: L += 1
            else:
                for t1 in s[sortedKeys[L]]:
                    for t2 in s[sortedKeys[R]]:
                        if len( set([ t1[0], t1[1], t2[0], t2[1] ]) ) == 4:
                            result.add(tuple(sorted([ t1[0], t1[1], t2[0], t2[1] ])))
                L, R = L + 1, R - 1
        # 这里还要进行去重, index不重复不等于结果不重复
        # 比如input Input: [-3,-2,-1,0,0,1,2,3], 0  Output: [[-3,0,1,2], [-3,0,1,2], ...]
        return map(list, set([tuple(sorted([nums[t[0]], nums[t[1]], nums[t[2]], nums[t[3]]])) for t in result]) )