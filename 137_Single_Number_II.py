# 2015-02-09 Runtime: 191 ms

class Solution:
    # @param A, a list of integer
    # @return an integer
    def singleNumber(self, A):
        # numbers in A are 32-bit integers in C format, most significant bit == 0 means positive, 1 means negative.
        # positive numbers are easy to handle.
        # For negative numbers, they are represented as complement 补码, e.g.  x= -12345, 
        # bit[31] is 1, bit[30] ~ bit[0] are 11...11(31 bits) - (-x) + 1, let y = 11...11 - (-x) + 1  
        bit = [0 for i in xrange(32)]
        # bit[0] is the least significant bit, bit[0]是最低位
        for number in A:
            for i in xrange(32):
                if (1 << i) & number == 1 << i: bit[i] += 1 
        res = 0
        if bit[31] % 3 == 0: # target number is positive
            for i in xrange(31):
                if bit[i] % 3 == 1: res += 1 << i
        else: # target number is negative
            for i in xrange(31):
                if bit[i] % 3 == 0: res += 1 << i # now res = 11..11 - y
            res = -(res + 1) # now res = -(11..11 - y + 1) = x
        return res