# 2015-07-31  Runtime: 304 ms

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
        # add every two numbers to get triplet (sum, firstIndex, secondIndex)
        d = collections.defaultdict(list)
        for i in xrange(len(nums)):
            for j in xrange(i + 1, len(nums)):
                d[nums[i] + nums[j]].append((i, j))

        # now it's a 2sum problem, use two pointers
        result = set()
        L, R = 0, len(d) - 1
        key = sorted(d.keys())
        while L <= R:
            if key[L] + key[R] == target:
                for t1 in d[key[L]]:
                    for t2 in d[key[R]]:
                        if t1[0] not in (t2[0], t2[1]) and t1[1] not in (t2[0], t2[1]):
                            result.add(tuple(sorted([nums[t1[0]], nums[t1[1]], nums[t2[0]], nums[t2[1]]])))
                L, R = L + 1, R - 1
            elif key[L] + key[R] < target:
                L += 1
            else:
                R -= 1
        return [list(item) for item in result]