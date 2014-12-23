# 2014-12-23  Runtime: 344 ms
class Solution:
    # @param num, a list of integers
    # @return an integer
    def majorityElement(self, num):
        appearTimes, N = {}, len(num)
        for i in num:
            appearTimes[i] = 1 if i not in appearTimes else appearTimes[i] + 1
        for key in appearTimes:
            if appearTimes[key] > N / 2: 
                return key