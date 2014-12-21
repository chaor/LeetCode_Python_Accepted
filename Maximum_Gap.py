# 2014-12-20  Runtime: 224 ms
class Solution:
    # @param num, a list of integer
    # @return an integer
    def maximumGap(self, num):
        N = len(num)
        if N < 2: return 0
        
        # put these numbers into different segments (buckets), 
        # there will be N buckets at most, e.g. num = [1, 5, 9, 13, 17]
        # 把这些数放到不同的段(也就是桶)内，最多N个桶，
        # 当这些数是等差数列的时候，比如num = [1, 5, 9, 13, 17]
        maxNum, minNum = max(num), min(num)
        bucketLen = int(math.ceil((maxNum - minNum) * 1.0 / (N - 1)))
        # buckets[i]'s range is [minNum + i * bucketLen, minNum + (i + 1) * bucketLen)
        buckets = [[] for i in xrange(N)]
        for k in num:
            buckets[(k - minNum) / bucketLen].append(k)
        
        # find out maxGap, the minimum maxGap will be bucketLen if num is arithmetic sequence.
        # maxGap comes from two numbers from adjacent buckets
        # 当num是等差数列时，maxGap最小，也就是bucket长度
        # maxGap是相邻两个bucket中的数的差
        maxGap, i, j = -1, 0, 1
        while j < N:
            if buckets[i] and buckets[j]: # both non-empty, 两个桶都非空
                maxGap = max(maxGap, min(buckets[j]) - max(buckets[i]))
                i, j = j, j + 1
            elif not buckets[i] and buckets[j]:
                i, j = j, j + 1
            elif buckets[i] and not buckets[j]:
                j += 1
            else:
                i, j = j + 1, j + 2
        return maxGap