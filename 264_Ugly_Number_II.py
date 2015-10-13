# 2015-10-13  Runtime: 64 ms

# Use class variable ugly to record previous result
# note here Solution.ugly and self.ugly refer to the same object, but Solution.t2 and self.t2
# will refer to different objects only t2's value has been changed. 
# In other words, mutable, same, unmutable, different.
class Solution(object):
    ugly = [1]
    t2, t3, t5 = 0, 0, 0  # pointer t2, t3, t5, any numbers before this have been added by ugly list
    
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        for i in xrange(len(self.ugly), n):
            self.ugly.append(min(self.ugly[Solution.t2] * 2, self.ugly[Solution.t3] * 3, self.ugly[Solution.t5] * 5))
            if self.ugly[-1] == self.ugly[Solution.t2] * 2: Solution.t2 += 1
            if self.ugly[-1] == self.ugly[Solution.t3] * 3: Solution.t3 += 1
            if self.ugly[-1] == self.ugly[Solution.t5] * 5: Solution.t5 += 1
        return self.ugly[n - 1]