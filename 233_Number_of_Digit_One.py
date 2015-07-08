# 2015-07-07  Runtime: 48 ms
class Solution:
    # @param {integer} n
    # @return {integer}
    def countDigitOne(self, n):
        # thanks to https://leetcode.com/discuss/44281/4-lines-o-log-n-c-java-python
        # 我们分别计算每一个的1出现的次数，m = [1, 10, 100, ..., 1000000000], 因为int32限制，m最大是1000000000
        # 当m=100时，算的是百位的1出现的次数，它等于百位左边的组合数目乘以百位右边的组合数目
        # 比如n = 3141592时，百位左边组合数目是3142种，即n / m + 1，百位右边组合数目是100，即m，
        # 所以百位的1出现次数是(n / m + 1) * m
        # 注意一下特殊情况，百位是0时，左边只有n / m * m种，右边还是100种
        # 百位是1时，要额外加上右边的组合数目不到100种的情况，是n % m + 1种
        # 把特殊情况综合一下，组合数是 (n / m + 8) / 10 * m种，再加上(n % m + 1) * (n / m % 10 == 1)种
        return sum((n / m + 8) / 10 * m + (n % m + 1) * (n / m % 10 == 1) for m in [10 ** i for i in xrange(10)])