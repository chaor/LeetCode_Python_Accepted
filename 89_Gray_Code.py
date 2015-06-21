# 2015-06-21  Runtime: 56 ms
class Solution:
    # @param {integer} n
    # @return {integer[]}
    def grayCode(self, n):
        # from wikipedia, https://en.wikipedia.org/wiki/Gray_code
        # binaryToGray: return (num >> 1) ^ num, i.e. (num / 2) XOR num
        # grayToBinary:
        # unsigned int mask;
        # for (mask = num >> 1; mask != 0; mask = mask >> 1)
        #     num = num ^ mask;
        # return num;
        return [(i >> 1) ^ i for i in xrange(2 ** n)] 