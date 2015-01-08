2014-01-08  Runtime: 96 ms

class Solution:
    # @return an integer
    def trailingZeroes(self, n):
        # just count how many factor 5 in n!, 
        # notice that for 625!, the number of factor 5 is 125 + 25 + 5 + 1, 
        # 1 stands for 625, 5 stands for 625, 500, 375, 250, 125, and so on.
        # 看一下n!里面有几个因数5就行了, 比如625!中因数5的个数是125 + 25 + 5 + 1
        # 1对应625, 5对应625, 500, 375, 250, 125, 以此类推。
        res = 0
        while n:
            n /= 5
            res += n
        return res