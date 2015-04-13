# 2015-04-13  Runtime: 50 ms  

class Solution:
    # @return a string
    def getPermutation(self, n, k):
        k -= 1
        result = ''
        numberPool = [str(i) for i in xrange(1, n+1)]
        for i in reversed(xrange(n)): # from n-1 to 0
            fac = math.factorial(i)
            result += numberPool[k / fac]
            del numberPool[k / fac]
            k %= fac
        return result