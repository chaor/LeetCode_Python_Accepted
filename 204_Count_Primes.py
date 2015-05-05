# 2015-05-04  Runtime: 1189 ms

class Solution:
    # @param {integer} n
    # @return {integer}
    def countPrimes(self, n):
        # http://en.wikipedia.org/wiki/Sieve_of_Eratosthenes, see Algorithm description, step 1 - 4
        # numberPool[N] = 0 means number N is not prime, 1 means N is prime
        p, numberPool = 1, [0, 0] + [1 for i in xrange(2, n)]
        for i in xrange(2, n):
            if numberPool[i]:
                p = i
                # keep prime p, remove 2p, 3p, 4p, 5p...
                for k in xrange(2, (n - 1) / p + 1): numberPool[k * p] = 0
        return sum(numberPool)